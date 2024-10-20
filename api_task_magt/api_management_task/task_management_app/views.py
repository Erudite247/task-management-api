from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    TaskViewSet provides 'CRUD' operations for the Task model.
    
    This viewset will automatically handle:
        - Listing all tasks (GET /api/tasks/)
        - Retrieving a task (GET /api/tasks/{id}/)
        - Creating a task (POST /api/tasks/)
        - Updating a task (PUT /api/tasks/{id}/)
        - Deleting a task (DELETE /api/tasks/{id}/)
    """

    queryset = Task.objects.all()  # A query for retrieving all tasks
    serializer_class = TaskSerializer  # Specifies which serializer to use
