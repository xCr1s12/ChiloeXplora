from django.urls import path
from .views import cucaoView

app_name = 'cucao'

urlpatterns = [
    path("", cucaoView.as_view(), name="Cucao") 
]