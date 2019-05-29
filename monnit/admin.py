from django.contrib import admin

# Register your models here.
from .models import Temperature
from .models import Door
from .models import Motion
from .models import Light


admin.site.register(Temperature)
admin.site.register(Door)
admin.site.register(Motion)
admin.site.register(Light)