from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'task_text', 'task_status']


    def validate(self, data):
        # Verifique se todos os campos necessários estão presentes
        if 'task_text' not in data or 'task_status' not in data:
            raise serializers.ValidationError("Todos os campos são obrigatórios")
        return data