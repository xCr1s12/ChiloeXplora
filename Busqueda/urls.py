from django.urls import path
from .views import Buscadorview

app_name = 'Buscar'

urlpatterns = [
    path("", Buscadorview.as_view(), name="Buscar") 
]
