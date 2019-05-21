from django.shortcuts import render
from rest_framework import generics
from .models import Temperature
from .serializers import TemperatureSerializer
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
