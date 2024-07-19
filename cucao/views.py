from django.shortcuts import render
from django.views.generic import View

class cucaoView(View):
    def get(self, request,*args, **kwargs):
        query = request.GET.get('q')
        context = {
            'query': query,
        }
        return render(request, "Notas_Cucao/notas_cucao.html",context )