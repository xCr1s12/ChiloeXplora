from django.shortcuts import render,redirect
from django.views.generic import View

class Buscadorview(View):
    def get(self, request,*args, **kwargs):
        context = {}
        return render(request, "Buscar/Buscar.html",context )