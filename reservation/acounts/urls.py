
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('login/', views.AccountLogin.as_view(), name='login'),
    path('logout/', views.AccountLogout.as_view(), name='logout'),
    #path('info2/',views.info2, name='info2'),
    #path('add/',views.add, name='add'),
    #path('addproduct/', views.addproduct, name='addproduct'),
]
