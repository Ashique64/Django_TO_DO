from django.db import models

# Create your models here.

class ToDoItems(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    