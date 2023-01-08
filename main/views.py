from unittest import result
from urllib import response
from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

from weasyprint import HTML
from django.template.loader import render_to_string
import tempfile
import codecs
from datetime import datetime
from django.template import Context, Template


# pdf
def pdf_sku(request, sku_id):
        sku = Sku.objects.get(id=sku_id)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="МК.pdf"'
        template = render_to_string('main/pdf_sku.html', {'sku': sku},)
        html = HTML(string=template,base_url=request.build_absolute_uri())
        result = html.write_pdf()

        with tempfile.NamedTemporaryFile(delete=True) as output:
            output.write(result)
            output.flush
            output = open(output.name,'rb')
            response.write(output.read())
      

        return response   
       

def search_sku(request):
    if request.method == "POST":
      searched = request.POST['searched']
      sku = Sku.objects.filter(num__contains = searched)
      return render(request, 'main/search_sku.html', {'searched':searched, 'sku':sku})
    else:
      return render(request, 'main/search_sku.html',{'searched':searched, 'sku':sku})

# SELECT sku_id from main_sku_raw where raw_id=32
def gen(request,change_id):
    change = Change.objects.get(id=change_id)
    sku = Sku.objects.filter(raw = change.raw_current)
    return render(request, 'main/gen.html', {'change':change,'sku':sku,})

def change(request,sku_id):
    sku = Sku.objects.get(id=sku_id)
    list_change = Change.objects.filter(raw_current__in = sku.raw.all())
    return render(request, 'main/change.html', {'sku':sku,'list_change':list_change,'change':change,})

   
def delete_sku(request, sku_id):
    sku = Sku.objects.get(id=sku_id)
    sku.delete()
    return redirect('list_sku')


def delete_raw(request, raw_id):
    raw = Raw.objects.get(id=raw_id)
    raw.delete()
    return redirect('list_raw')

def update_sku(request, sku_id):
    sku = Sku.objects.get(id=sku_id)
    form = SkuForm(request.POST or None,request.FILES or None, instance=sku)
    if form.is_valid():
        form.save()
        return redirect('list_sku')

    return render(request, 'main/update_sku.html', {'sku': sku, 'form': form})


def update_raw(request, raw_id):
    raw = Raw.objects.get(id=raw_id)
    form = RawForm(request.POST or None, instance=raw)
    if form.is_valid():
        form.save()
        return redirect('list_raw')

    return render(request, 'main/update_raw.html', {'raw': raw, 'form': form})


def status(request):
    changes = Change.objects.all()
    raws = Raw.objects.all()
    return render(request, 'main/status.html',{'changes': changes,'raws': raws})


def add(request):
    return render(request, 'main/add.html')


def list_raw(request):
    raws = Raw.objects.all()
    return render(request, 'main/list_raw.html', {'raws': raws})


def list_sku(request):
    skus = Sku.objects.all()
    return render(request, 'main/list_sku.html', {'skus': skus})


def show_sku(request, sku_id):
    sku = Sku.objects.get(id=sku_id)
    return render(request, 'main/show_sku.html', {'sku': sku})

def add_raw(request):
    if request.method == 'POST':
        form = RawForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, ' Артикул добавлен ')
            return HttpResponseRedirect('/add_raw')
    else:
        if 'submit' in request.GET:
            submit = True
        print('hi')
        return render(request, 'main/add_raw.html')

def add_sku(request):
    submit = False
    if request.method == 'POST':
        form = SkuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_sku?submit=True')
    else:
        form = SkuForm
        if 'submit' in request.GET:
            submit = True
    return render(request, 'main/add_sku.html', {'form': form, 'submit': submit})


def add(request):
    submit = False
    if request.method == 'POST':
        form = ChangeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add?submit=True')
    else:
        form = ChangeForm
        if 'submit' in request.GET:
            submit = True
    return render(request, 'main/add.html', {'form': form, 'submit': submit})

