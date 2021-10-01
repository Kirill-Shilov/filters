from django.db import models

# Create your models here.
class Table(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    distance = models.IntegerField()
