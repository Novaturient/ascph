from django.db import models

# Create your models here.
class Temperature(models.Model):
    dateRead = models.DateTimeField(unique=True)
    reading = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.dateRead} {self.reading}"

class Door(models.Model):
    dateRead = models.DateTimeField(unique=True)
    reading = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.dateRead} {self.reading}"

class Motion(models.Model):
    dateRead = models.DateTimeField(unique=True)
    reading = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.dateRead} {self.reading}"

class Light(models.Model):
    dateRead = models.DateTimeField(unique=True)
    reading = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.dateRead} {self.reading}"

class Vibration(models.Model):
    dateRead = models.DateTimeField(unique=True)
    reading = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.dateRead} {self.reading}"

class Sensor(models.Model):
    DataMessageGUID = models.CharField(max_length=255, primary_key=True)
    SensorID = models.CharField(max_length=7)
    MessageDate = models.DateTimeField()
    State = models.IntegerField()
    SignalStrength = models.IntegerField()
    Voltage = models.CharField(max_length=255)
    Battery =  models.IntegerField()
    Data = models.CharField(max_length=255)
    DisplayData = models.CharField(max_length=255)
    PlotValue = models.CharField(max_length=255)
    MetNotificationRequirements = models.CharField(max_length=35)
    GatewayID = models.CharField(max_length=7)
    DataValues = models.CharField(max_length=255)
    DataTypes = models.CharField(max_length=255)
    PlotValues = models.CharField(max_length=255)
    PlotLabels = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.DataMessageGUID} {self.SensorID}"