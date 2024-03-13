from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    starting_weight = serializers.FloatField(write_only=True, required=False)
    current_weight = serializers.FloatField(write_only=True, required=False)
    desired_weight = serializers.FloatField(write_only=True, required=False)
    starting_muscle = serializers.FloatField(write_only=True, required=False)
    current_muscle = serializers.FloatField(write_only=True, required=False)
    desired_muscle = serializers.FloatField(write_only=True, required=False)

    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'email', 'starting_weight', 'current_weight', 'desired_weight', 'starting_muscle', 'current_muscle', 'desired_muscle']

    def create(self, validated_data):
        starting_weight = validated_data.pop('starting_weight', None)
        current_weight = validated_data.pop('current_weight', None)
        desired_weight = validated_data.pop('desired_weight', None)
        starting_muscle = validated_data.pop('starting_muscle', None)
        current_muscle = validated_data.pop('current_muscle', None)
        desired_muscle = validated_data.pop('desired_muscle', None)
        
        user = User.objects.create_user(**validated_data)
        if starting_weight is not None:
            user.starting_weight = starting_weight
        if current_weight is not None:
            user.current_weight = current_weight
        if desired_weight is not None:
            user.desired_weight = desired_weight
        if starting_muscle is not None:
            user.starting_muscle = starting_muscle
        if current_muscle is not None:
            user.current_muscle = current_muscle
        if desired_muscle is not None:
            user.desired_muscle = desired_muscle
        
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.current_weight = validated_data.get('current_weight', instance.current_weight)
        instance.desired_weight = validated_data.get('desired_weight', instance.desired_weight)
        instance.current_muscle = validated_data.get('current_muscle', instance.current_muscle)
        instance.desired_muscle = validated_data.get('desired_muscle', instance.desired_muscle)
        instance.save()
        return instance