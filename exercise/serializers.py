from rest_framework import serializers
from .models import WorkOut

class WorkOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOut
        fields = ['text', 'description', 'repetitions', 'sets', 'complete']