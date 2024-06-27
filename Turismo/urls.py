from django.urls import path
from .views import TurismoListViews

app_name = ["Turismo"]

urlpatterns = {

    path("",TurismoListViews.as_view(), name="home")   
}