from django.db import models
from django.urls import reverse

# Create your models here.

    
class TodoItem(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)