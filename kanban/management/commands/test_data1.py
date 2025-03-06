import json
import pytz
from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils.timezone import now
from kanban.models import Project, Board, Column, Card, Movement, CFD  # Update 'app' with your actual app name

IST = pytz.timezone("Asia/Kolkata")

class Command(BaseCommand):
    help = "Simulates board movements over 2 weeks and generates CFD data"

    def handle(self, *args, **kwargs):
        """Main function to execute the simulation"""
        self.stdout.write(self.style.SUCCESS("Starting board movement simulation..."))

        project, board = self.setup_project_board()
        columns = self.setup_columns(project, board)
        cards = self.setup_cards(project, board, columns["To Do"])
        
        self.simulate_movements(project, board, columns, cards)

        self.stdout.write(self.style.SUCCESS("Board movement simulation completed!"))

    def setup_project_board(self):
        """Create a project and board if not exists"""
        project, _ = Project.objects.get_or_create(name="Agile Transformation")
        board, _ = Board.objects.get_or_create(project=project, name="Sprint Board")
        return project, board

    def setup_columns(self, project, board):
        """Create board columns"""
        column_names = ["To Do", "WIP", "Deploy", "Done"]
        columns = {}
        for idx, name in enumerate(column_names, start=1):
            column, _ = Column.objects.get_or_create(project=project, board=board, name=name, position=idx)
            columns[name] = column
        return columns

    def setup_cards(self, project, board, todo_column):
        """Create 50 cards in the 'To Do' column"""
        cards = []
        for i in range(1, 51):
            card, _ = Card.objects.get_or_create(
                project=project, board=board, column=todo_column, title=f"Task {i}"
            )
            cards.append(card)
        return cards

    def simulate_movements(self, project, board, columns, cards):
        """Simulate card movements over 2 weeks and generate CFD data"""
        start_date = now().astimezone(IST)
        current_date = start_date

        for day in range(14):  # 2 weeks
            move_count = (day + 1) * 3  # Move 3 cards per day

            for i in range(min(move_count, len(cards))):
                card = cards[i]
                
                # Determine next column
                if card.column == columns["To Do"]:
                    new_column = columns["WIP"]
                elif card.column == columns["WIP"]:
                    new_column = columns["Deploy"]
                elif card.column == columns["Deploy"]:
                    new_column = columns["Done"]
                else:
                    continue  # Skip if already in "Done"

                # Create Movement Record
                Movement.objects.create(
                    project=project,
                    board=board,
                    card=card,
                    from_column=card.column,
                    to_column=new_column,
                    moved_at=current_date
                )

                # Update the Card's Column
                card.column = new_column
                card.save()

            # Generate CFD snapshot for the day
            self.generate_cfd_snapshot(project, board, current_date)

            # Move to the next day
            current_date += timedelta(days=1)

    def generate_cfd_snapshot(self, project, board, timestamp):
        """Generate CFD data for the given timestamp"""
        column_counts = {
            "To Do": Card.objects.filter(project=project, board=board, column__name="To Do").count(),
            "WIP": Card.objects.filter(project=project, board=board, column__name="WIP").count(),
            "Deploy": Card.objects.filter(project=project, board=board, column__name="Deploy").count(),
            "Done": Card.objects.filter(project=project, board=board, column__name="Done").count(),
        }

        CFD.objects.create(
            project=project,
            board=board,
            data_timestamp=timestamp,
            column_card_counts=json.dumps(column_counts)
        )

        self.stdout.write(self.style.NOTICE(f"CFD Snapshot on {timestamp}: {column_counts}"))
