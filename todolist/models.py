from django.db import models

class Task(models.Model):
    task_text = models.CharField(max_length=200)
    task_status = models.BooleanField(default=False)

    def __str__(self):
        return self.task_text
    
    def is_done(self):
        return self.task_status
        
