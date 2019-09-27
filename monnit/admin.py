from django.contrib import admin

# Register your models here.
from .models import Temperature
from .models import Door
from .models import Motion
from .models import Light
from .models import Vibration
from .models import Sensor


admin.site.register(Temperature)
admin.site.register(Door)
admin.site.register(Motion)
admin.site.register(Light)
admin.site.register(Vibration)
admin.site.register(Sensor)