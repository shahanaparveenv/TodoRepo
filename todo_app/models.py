from django.db import models

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=20)
    subject=models.CharField(max_length=20)
    date=models.DateField()