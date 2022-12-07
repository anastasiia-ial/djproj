from django.shortcuts import render
from .models import Raw, Change

def status(request):
    changes=Change.objects.all()
    return render(request, 'main/status.html',{'changes':changes})
    
def gen(request):
    return render(request, 'main/gen.html')

def add(request):
   return render(request, 'main/add.html')
    
def list(request):
    raws=Raw.objects.all()
    return render(request, 'main/list.html',{'raws':raws})

