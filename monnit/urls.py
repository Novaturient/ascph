from django.urls import path
from .views import TemperatureView
from .views import DoorView
from .views import MotionView
from .views import LightView

urlpatterns = [
    path('temperatures/',TemperatureView.as_view(),name="temperatures-all"),
    path('doors/',DoorView.as_view(),name="doors-all"),
    path('motion/',MotionView.as_view(),name="motion-all"),
    path('light/',LightView.as_view(),name="light-all")
]