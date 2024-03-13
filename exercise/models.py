from django.db import models

# Create your models here.
class ToDo(models.Model):
    workoutName = models.CharField(max_length = 100)

    def __str__(self):
        return self.workoutName

class WorkOut(models.Model):
    text = models.CharField(max_length =200)
    description = models.TextField(default='Default')
    repetitions = models.PositiveBigIntegerField(default=10)
    sets = models.PositiveBigIntegerField(default=4)
    complete = models.BooleanField()

    def __str__(self):
        return f"{self.text} - {self.description} - {self.repetitions} - {self.sets}"
        
    