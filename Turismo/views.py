from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class TurismoListViews(View):
    def get(self, request,*args ,**kwargs):
        context = {
            
        }
        return render(request,"asd/asdas.html",context)