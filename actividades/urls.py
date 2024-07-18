from django.urls import path
from .views import actividad

app_name = 'actividades'

urlpatterns = [
    path("", actividad.as_view(), name="actividades") 
]