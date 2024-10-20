
from .models import Task
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    """
   This serializer handles the conversion of Task model instances into JSON format and 
   ensures that input data is properly validated when creating or updating tasks.

    """

    class Meta:
        model = Task
        fields = '__all__'  # This serializer automatically incorporates all fields from the model.

