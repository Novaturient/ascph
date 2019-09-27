from django.shortcuts import render
from rest_framework import generics
from .models import Temperature
from .serializers import TemperatureSerializer
from .models import Door
from .serializers import DoorSerializer
from .models import Motion
from .serializers import MotionSerializer
from .models import Light
from .serializers import LightSerializer
from .models import Vibration
from .serializers import VibrationSerializer
from .models import Sensor
from .serializers import SensorSerializer
from rest_framework.response import Response


# Create your views here.
class TemperatureView(generics.ListCreateAPIView):
    """
    Provides a get and post method
    """
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

    def post(self,request):
        temp = Temperature.objects.create(
            dateRead=request.data["dateRead"],
            reading=request.data["reading"]
        )
        return Response(
            data=TemperatureSerializer(temp).data, 
        )

class DoorView(generics.ListCreateAPIView):
    """
    Provides a get and post method
    """
    queryset = Door.objects.all()
    serializer_class = DoorSerializer

    def post(self,request):
        door = Door.objects.create(
            dateRead=request.data["dateRead"],
            reading=request.data["reading"]
        )
        return Response(
            data=DoorSerializer(door).data, 
        )

class MotionView(generics.ListCreateAPIView):
    """
    Provides a get and post method
    """
    queryset = Motion.objects.all()
    serializer_class = MotionSerializer

    def post(self,request):
        motion = Motion.objects.create(
            dateRead=request.data["dateRead"],
            reading=request.data["reading"]
        )
        return Response(
            data=MotionSerializer(motion).data, 
        )

class LightView(generics.ListCreateAPIView):
    """
    Provides a get and post method
    """
    queryset = Light.objects.all()
    serializer_class = LightSerializer

    def post(self,request):
        light = Light.objects.create(
            dateRead=request.data["dateRead"],
            reading=request.data["reading"]
        )
        return Response(
            data=LightSerializer(light).data, 
        )

class VibrationView(generics.ListCreateAPIView):
    """
    Provides a get and post method
    """
    queryset = Vibration.objects.all()
    serializer_class = VibrationSerializer

    def post(self,request):
        vibration = Vibration.objects.create(
            dateRead=request.data["dateRead"],
            reading=request.data["reading"]
        )
        return Response(
            data=VibrationSerializer(vibration).data, 
        )

class SensorView(generics.ListCreateAPIView):
    """
    Provides a get and post method
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self,request):
        sensor = Sensor.objects.create(
            DataMessageGUID = request.data["DataMessageGUID"],
            SensorID = request.data["SensorID"],
            MessageDate = request.data["MessageDate"],
            State = request.data["State"],
            SignalStrength = request.data["SignalStrength"],
            Voltage = request.data["Voltage"],
            Battery =  request.data["Battery"],
            Data = request.data["Data"],
            DisplayData = request.data["DisplayData"],
            PlotValue = request.data["PlotValue"],
            MetNotificationRequirements = request.data["MetNotificationRequirements"],
            GatewayID = request.data["GatewayID"],
            DataValues = request.data["DataValues"],
            DataTypes = request.data["DataTypes"],
            PlotValues = request.data["PlotValues"],
            PlotLabels = request.data["PlotLabels"]
        )
        return Response(
            data=SensorSerializer(sensor).data, 
        )