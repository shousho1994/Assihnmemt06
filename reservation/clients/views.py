
from django.shortcuts import render,HttpResponse,redirect,reverse
from.forms import ProductForm
from django.shortcuts import render, redirect
from .forms import ProductForm,ClientForm

from .models import Client


products=[]
def index(request):
    return HttpResponse("<h>Clients Home Page</h>")

def info2(request):
    return render(request, "base.html", )
def add(request):
    return render(request,"add.html",)



def addproduct(request):

        f=ProductForm()
        return render(request,'product.html',{'productform':f})


def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            if 'client_count' in request.session:
                request.session['client_count'] += 1
            else:
                request.session['client_count'] = 1
            return redirect('add_client.html')
    else:
        form = ClientForm()
    return render(request, 'add_client.html', {'form': form})

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client.html', {'clients': clients})