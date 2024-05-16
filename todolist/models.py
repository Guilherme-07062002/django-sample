from django.db import models

class Task(models.Model):
    task_text = models.CharField(max_length=200)
    task_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_text
    
    def is_done(self):
        return self.task_status
        
        
