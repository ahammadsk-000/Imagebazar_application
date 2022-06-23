from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    path('aboutus',views.show_about_page,name='aboutus'),
    path('',views.show_home_page,name='home'),
]