# Generated by Django 5.0.3 on 2024-03-13 16:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0003_remove_workout_todo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkoutPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default='Default')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutPlanWorkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repetitions', models.PositiveIntegerField(default=10)),
                ('sets', models.PositiveIntegerField(default=4)),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercise.workout')),
                ('workout_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercise.workoutplan')),
            ],
        ),
        migrations.AddField(
            model_name='workoutplan',
            name='workouts',
            field=models.ManyToManyField(through='exercise.WorkoutPlanWorkout', to='exercise.workout'),
        ),
    ]
