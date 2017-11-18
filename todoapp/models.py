from django.db import models
from datetime import datetime

class Todo(models.Model):
     title = models.CharField(max_length=150)
     created_at = models.DateTimeField(default=datetime.now,blank=True)
     text = models.TextField()

     def __str__(self):
        return self.title
# Create your models here.
