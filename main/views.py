from django.shortcuts import render
from .models import Raw
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
    
def list(request):
    raws=Raw.objects.all()
    return render(request, 'main/list.html',{'raws':raws})




