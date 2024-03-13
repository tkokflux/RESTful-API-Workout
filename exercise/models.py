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
        
class WorkoutPlan(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(default='Default')
    workouts = models.ManyToManyField(WorkOut, through='WorkoutPlanWorkout')

    def __str__(self):
        return self.name

class WorkoutPlanWorkout(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    workout = models.ForeignKey(WorkOut, on_delete=models.CASCADE)
    repetitions = models.PositiveIntegerField(default=10)
    sets = models.PositiveIntegerField(default=4)

    def __str__(self):
        return f"{self.workout_plan.name} - {self.workout.text} - Reps: {self.repetitions}, Sets: {self.sets}"  