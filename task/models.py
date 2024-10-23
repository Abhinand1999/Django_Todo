from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateField(null=False, blank=False)
    due_time = models.TimeField(null=False, blank=False)
    completed = models.BooleanField(default=False)
    def __str__(self) -> str:
        return f'{self.title}'