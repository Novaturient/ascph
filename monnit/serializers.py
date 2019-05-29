from rest_framework import serializers
from .models import Temperature
from .models import Door
from .models import Motion
from .models import Light


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = '__all__'

class DoorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Door
        fields = '__all__'

class MotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motion
        fields = '__all__'

class LightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Light
        fields = '__all__'