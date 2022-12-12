from django.shortcuts import render
from .models import *
from .forms import RawForm


def add_raw(request):
    if request.method == 'POST':
        form = RawForm(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request, 'main/add_raw.html')

    else:
         print ('hi')
         return render(request, 'main/add_raw.html')


def status(request):
    # changes=Change.objects.all()
    return render(request, 'main/status.html')
    
def gen(request):
    return render(request, 'main/gen.html')

def add(request):
   return render(request, 'main/add.html')
    
def list_raw(request):
    raws=Raw.objects.all()
    return render(request, 'main/list_raw.html',{'raws':raws})

def list_sku(request):
    skus=Sku.objects.all()
    return render(request, 'main/list_sku.html',{'skus':skus})

def show_sku(request, sku_id):
    sku = Sku.objects.get(id=sku_id)
    return render(request, 'main/show_sku.html',{'sku':sku})

