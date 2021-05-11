from django.db import models

# Create your models here.
class Exercise(models.Model):
    name = models.CharField(max_length=30, unique=True)
    weight = models.FloatField(default=0.0)
    reps = models.IntegerField(default=0)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return self.name
