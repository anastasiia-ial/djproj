from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect


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

# def add_sku(request):
#     form = SkuForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#     # if request.method == 'POST':
#     #     form = SkuForm (request.POST)
#     #     context = {'form' : form}
#     #     if form.is_valid():
#     #         form.save()
#     return render(request,'main/add_sku.html',{'form':form})  


def add_sku(request):
    submit =  False
    if request.method == 'POST':
        form = SkuForm (request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_sku?submit=True')
    else:
          form = SkuForm
          if 'submit' in request.GET:
              submit = True
    return render(request,'main/add_sku.html',{'form':form, 'submit':submit})  

    