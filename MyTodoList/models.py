from django.db import models

# Create your models here.
class Todo(models.Model):
    Booktitle=models.CharField(max_length=500)
    def __str__(self):
        return self.Booktitle
