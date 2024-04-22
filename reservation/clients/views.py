from django.shortcuts import render,HttpResponse


def index(request):
    return HttpResponse("<h>Clients Home Page</h>")

def info2(request):
    return render(request, "base.html", )
def add(request):
    return render(request,"add.html",)