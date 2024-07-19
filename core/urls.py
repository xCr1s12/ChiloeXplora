from .views import Homeview
from django.contrib import admin
from django.urls import path, include
from Users import views as user_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Homeview.as_view(), name='inicio'),
    path('comentarios/', include('comentarios.urls', namespace='comentarios')),
    path("Lugares_Recomendados/", include("Turismo.urls", namespace='Recomendados')),
    path("Buscar/Notas_Cucao/", include("cucao.urls", namespace='cucao')),
    path("Buscar/", include("Busqueda.urls", namespace='Buscador')),
    path('login/registro/', user_views.registro_usuario, name='registro'),  
    path('login/', user_views.login_usuario, name='login'),
    path('logout/', user_views.logout_usuario, name='logout'),
    path("actividades/", include("actividades.urls", namespace='actividades')),
    path('perfil/', include("perfil.url", namespace="perfil")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)