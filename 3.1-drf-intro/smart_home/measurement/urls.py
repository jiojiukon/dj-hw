from django.urls import path
from .views import SensorView, MeasurementView, SmartHomeView

urlpatterns = [
    path('sensors/', SmartHomeView.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
    path('measurements/', MeasurementView.as_view())
]
