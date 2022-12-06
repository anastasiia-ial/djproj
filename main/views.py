from django.shortcuts import render
from .models import Raw, Change

def status(request):
    return render(request, 'main/status.html')
    
def gen(request):
    return render(request, 'main/gen.html')

def add(request):
   return render(request, 'main/add.html')
    
def list(request):
    raws=Raw.objects.all()
    return render(request, 'main/list.html',{'raws':raws})

