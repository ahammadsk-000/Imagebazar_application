from django.shortcuts import render
from .models import Image,Category
# Create your views here.
def show_about_page(request):
    return render(request,'show_about_page.html')

def show_home_page(request):

    cats = Category.objects.all()
    images = Image.objects.all()
    data = {'images':images,'cats':cats}


    return render(request,'home.html',data)