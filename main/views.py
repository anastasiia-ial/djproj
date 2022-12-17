from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4


def pdf_sku (request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize= A4,bottomup= 0)
    textobj = c.beginText()
    textobj.setTextOrigin (cm,cm)
    textobj.setFont('Helvetica', 14)

    skus = Sku.objects.all()
    lines=[]
    # lines=[
    #     "line",
    #     "ht",
    #     "dfdfgd"
    # ]
    for sku in skus:
        lines.append (sku.num)
        lines.append (sku.name)
    #     lines.append (sku.raw)
        # lines.append (sku.weight)
        # lines.append (sku.photo)
    
    for line in lines:
        textobj.textLine(line)

    c.drawText(textobj)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='MK.pdf')

def delete_sku(request, sku_id):
    sku = Sku.objects.get(id=sku_id)
    sku.delete()
    return redirect ('list_sku')


def delete_raw(request, raw_id):
    raw = Raw.objects.get(id=raw_id)
    raw.delete()
    return redirect ('list_raw')
        
    # return render(request, 'main/update_raw.html',{'raw':raw})

def update_sku(request, sku_id):
    sku = Sku.objects.get(id=sku_id)
    form = SkuForm (request.POST or None, instance=sku)
    if form.is_valid():
            form.save()
            return redirect ('list_sku')
        
    return render(request, 'main/update_sku.html',{'sku':sku,'form':form})

def update_raw(request, raw_id):
    raw = Raw.objects.get(id=raw_id)
    form = RawForm (request.POST or None, instance=raw)
    if form.is_valid():
            form.save()
            return redirect ('list_raw')
        
    return render(request, 'main/update_raw.html',{'raw':raw, 'form':form})


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
        form = SkuForm (request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_sku?submit=True')
    else:
          form = SkuForm
          if 'submit' in request.GET:
              submit = True
    return render(request,'main/add_sku.html',{'form':form, 'submit':submit})  

    