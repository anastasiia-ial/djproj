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


# not working img 
def pdf_sku(request, sku_id):
        sku = Sku.objects.get(id=sku_id)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="MK.pdf"'
        template = render_to_string('main/pdf_sku.html', {'sku': sku})
        html = HTML(string=template)
        result = html.write_pdf()

        with tempfile.NamedTemporaryFile(delete=True) as output:
            output.write(result)
            output.flush
            output = open(output.name,'rb')
            response.write(output.read())
            # contents = contents.decode('utf-8', 'ignore')   

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
    # raw = Sku.objects.get(raw = '33' , id = sku.id)
    # all = Raw.objects.all()
    # raw = Sku.objects.filter(raw = all.num)
    list_change = Change.objects.all()
    # list_change  = Change.objects.filter(raw_current = sku.raw)
    # change = Change.objects.filter(raw_current = sku.raw)
    # change=Change.objects.all()
    # change_1 = Change.raw_current.get_object(change)
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
    form = SkuForm(request.POST or None, instance=sku)
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
    # submit = False
    if request.method == 'POST':
        form = RawForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, ' Артикул добавлен ')
            return HttpResponseRedirect('/add_raw')
            # return HttpResponseRedirect('/add_raw?submit=True')
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
            # messages.success (request, 'got it ')
            return HttpResponseRedirect('/add_sku?submit=True')
            # return HttpResponseRedirect('/add_sku')
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


# from io import StringIO
# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa


# def pdf_sku(request,sku_id):
#     sku = Sku.objects.get(id=sku_id)
#     template_path = 'main/pdf_sku.html'
#     context = {'sku': sku}
#     # Create a Django response object, and specify content_type as pdf
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="MK.pdf"'
#     # find the template and render it.
#     template = get_template(template_path)
#     html = template.render(context)
#     # create a pdf
#     # pisa_status = pisa.CreatePDF(
#     #    html, dest=response)
#     result = StringIO()
#     pisa_status = pisa.CreatePDF(StringIO(html.encode('utf-8')), result)
#     # if error then show some funny view
#     if pisa_status.err:
#        return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response


# def pdf_sku(request):
#     buf = io.BytesIO()
#     c = canvas.Canvas(buf, pagesize=A4, bottomup=0)

#     # textobj = c.beginText()
#     textobj = c.drawString(280,700,'sku.num')
#     textobj = c.drawString(280,400,'sku.num')
#     # textobj = c.drawString(280,700,)
#     # textobj = c.drawString(280,700,)
#     # textobj = c.drawString(280,700,)
#     # textobj.setTextOrigin(cm, cm)
#     # textobj.setFont('Helvetica', 14)
#     # img = c.drawImage(298,432)

#     skus = Sku.objects.all()
#     # lines = []
#     # lines=[
#     #     "line",
#     #     "ht",
#     #     "dfdfgd"
#     # ]
#     # for sku in skus:
#         # lines.append(sku.num)
#         # lines.append(sku.name)
#         # lines.append(sku.raw)
#         # lines.append(sku.weight)
#         # lines.append(sku.photo)

#     # for line in lines:
#         # textobj.textLine(line)
#         # img.drawInlineimage(img)
#     # c.drawString(textobj)
#     # c.drawInlineImage(img)
#     c.showPage()
#     c.save()
#     buf.seek(0)
#     return FileResponse(buf, as_attachment=True, filename='MK.pdf')
    # buf = io.BytesIO()
    # c = canvas.Canvas(buf, pagesize=A4, bottomup=0)
    # c.setTitle(sku.num+' '+sku.name)
    # # textobj = c.beginText()
    # # textobj.setTextOrigin(cm, cm)
    # # textobj.setFont('Helvetica', 14)

    # skus = Sku.objects.all()
    # lines = []
    # # lines=[
    # #     "line",
    # #     "ht",
    # #     "dfdfgd"
    # # ]
    # for sku in skus:
    #     lines.append(sku.num)
    #     lines.append(sku.name)
    # #     lines.append (sku.raw)
    #     # lines.append (sku.weight)
    #     # lines.append (sku.photo)

    # for line in lines:
    #     textobj.textLine(line)

    # c.drawText(textobj)
    # c.showPage()
    # c.save()
    # buf.seek(0)
    # return FileResponse(buf, as_attachment=True, filename='MK.pdf')


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
