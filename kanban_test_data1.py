import json
import pytz
from datetime import timedelta
from django.test import TestCase
from django.utils.timezone import now
from kanban.models import Project, Board, Column, Card, Movement, CFD

IST = pytz.timezone("Asia/Kolkata")

class ProjectBoardCFDTest(TestCase):

    def setUp(self):
        """Create a project, board, columns, and 50 cards"""
        self.project = Project.objects.create(name="Agile Transformation")
        self.board = Board.objects.create(project=self.project, name="Sprint Board")

        # Creating Columns
        self.todo = Column.objects.create(project=self.project, board=self.board, name="To Do", position=1)
        self.wip = Column.objects.create(project=self.project, board=self.board, name="WIP", position=2)
        self.deploy = Column.objects.create(project=self.project, board=self.board, name="Deploy", position=3)
        self.done = Column.objects.create(project=self.project, board=self.board, name="Done", position=4)

        # Creating 50 Cards in To Do
        self.cards = []
        for i in range(1, 51):
            card = Card.objects.create(project=self.project, board=self.board, column=self.todo, title=f"Task {i}")
            self.cards.append(card)

    def test_card_movements_and_cfd(self):
        """Simulate 2-week movements and generate CFD data"""
        start_date = now().astimezone(IST)
        current_date = start_date

        # Movement Simulation
        for day in range(14):  # 2 Weeks
            move_count = (day + 1) * 3  # Move 3 cards per day

            for i in range(min(move_count, len(self.cards))):
                card = self.cards[i]
                
                # Simulate movement through the workflow
                if card.column == self.todo:
                    new_column = self.wip
                elif card.column == self.wip:
                    new_column = self.deploy
                elif card.column == self.deploy:
                    new_column = self.done
                else:
                    continue  # Skip if already in "Done"

                # Create Movement Record
                Movement.objects.create(
                    project=self.project,
                    board=self.board,
                    card=card,
                    from_column=card.column,
                    to_column=new_column,
                    moved_at=current_date
                )

                # Update the Card's Column
                card.column = new_column
                card.save()

            # Generate CFD snapshot for the day
            self.generate_cfd_snapshot(current_date)
            
            # Move to the next day
            current_date += timedelta(days=1)

    def generate_cfd_snapshot(self, timestamp):
        """Generate CFD data for the given timestamp"""
        column_counts = {
            "To Do": Card.objects.filter(project=self.project, board=self.board, column=self.todo).count(),
            "WIP": Card.objects.filter(project=self.project, board=self.board, column=self.wip).count(),
            "Deploy": Card.objects.filter(project=self.project, board=self.board, column=self.deploy).count(),
            "Done": Card.objects.filter(project=self.project, board=self.board, column=self.done).count(),
        }

        CFD.objects.create(
            project=self.project,
            board=self.board,
            data_timestamp=timestamp,
            column_card_counts=json.dumps(column_counts)
        )

        # Print to console for debugging
        print(f"CFD Snapshot on {timestamp}: {column_counts}")
