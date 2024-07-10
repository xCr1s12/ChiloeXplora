from .views import Homeview
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Homeview.as_view(), name ="Inicio"),
    path("Lugares_Recomendados/", include("Turismo.urls", namespace='Recomendados')),
    path("Notas_Cucao/", include("cucao.urls", namespace='cucao')),
]
