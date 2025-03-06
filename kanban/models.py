from django.db import models
from django.utils.timezone import now
import pytz

IST = pytz.timezone("Asia/Kolkata")

class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=now)
    
    def __str__(self):
        return self.name


class Board(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="boards")
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.project.name} - {self.name}"


class Column(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="columns")
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="columns")
    name = models.CharField(max_length=255)
    position = models.PositiveIntegerField(help_text="Order of column in the board")
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.board.name} - {self.name}"


class Card(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="cards")
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="cards")
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name="cards")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.board.name} - {self.column.name} - {self.title}"


class Movement(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="movements")
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="movements")
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="movements")
    from_column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name="moved_from")
    to_column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name="moved_to")
    moved_at = models.DateTimeField(default=lambda: now().astimezone(IST))

    def __str__(self):
        return f"{self.card.title} moved from {self.from_column.name} to {self.to_column.name} on {self.moved_at}"


class CFD(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="cfd_data")
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="cfd_data")
    data_timestamp = models.DateTimeField(default=lambda: now().astimezone(IST))
    column_card_counts = models.JSONField(default=dict, help_text="JSON structure of column-wise card counts")

    def __str__(self):
        return f"CFD for {self.board.name} on {self.data_timestamp}"
