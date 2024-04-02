from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=35)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateField()
    due_time = models.TimeField()
    completed = models.BooleanField(default=False)


    # Returns a string representation of the model.
    #
    # The string is constructed from the 'title' field.
    #
    # Returns:
    #     str: A string representation of the model.
    def __str__(self) -> str:
        """Returns a string representation of the model."""
        return f'{self.title}'
