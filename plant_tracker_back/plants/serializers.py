from rest_framework import serializers
from .models import Plant

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['name', 'slug', 'room', 'last_time_watered', 'notes']
        extra_kwargs = {'slug': {'required': False}}
        
    def create(self, validated_data):
        instance = Plant.objects.create(**validated_data)
        return instance
