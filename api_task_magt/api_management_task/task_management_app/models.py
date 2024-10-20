from django.db import models

class Task(models.Model):
    """
    Task model representing a task in the Task Management system.
    
    Fields:
        - title: The title of the task (required).
        - description: A detailed description of the task (optional).
        - status: The current status of the task (choices: To Do, In Progress, Completed).
        - priority: The priority level of the task (choices: Low, Medium, High).
        - due_date: The deadline by which the task should be completed (optional).
        - category: A category to classify the task (optional).
        - created_at: The timestamp when the task was created (auto-generated).
        - updated_at: The timestamp when the task was last updated (auto-generated).
    """

    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('inprogress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='todo')
    priority = models.CharField(max_length=30, choices=PRIORITY_CHOICES, default='medium')
    due_date = models.DateField(null=True, blank=True)
    category = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """This returns the  task title as its string representation"""
        return self.title
