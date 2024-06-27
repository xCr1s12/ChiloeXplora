from django.views.generic import View 
from django.shortcuts import render

class Homeview(View):
    def get(self, request,*args ,**kwargs):
        context = {


        }
        return render(request,"Pagina_Principal\index.html",context)