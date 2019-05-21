from django.db import models

# Create your models here.
class Temperature(models.Model):
    dateRead = models.CharField(max_length=255)
    reading = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.dateRead} {self.reading}"

