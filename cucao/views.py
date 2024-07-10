from django.shortcuts import render
from django.views.generic import View

class cucaoView(View):
    def get(self, request,*args, **kwargs):
        context = {}
        return render(request, "Notas_Cucao/notas_cucao.html",context )