
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import  login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('info2/',views.info2, name='info2'),
    path('add/',views.add, name='add'),
    path('addproduct/', views.addproduct, name='addproduct'),
]
