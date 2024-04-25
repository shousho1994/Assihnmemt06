
from django.shortcuts import render,HttpResponse,redirect,reverse
from.forms import ProductForm



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