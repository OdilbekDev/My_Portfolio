from django.shortcuts import render
from .models import *

# Create your views here.
def Index(request):
    home = Home.objects.last()
    about = About_Us.objects.last()
    service1 = Services.objects.get(id=1)
    service2 = Services.objects.get(id=2)
    service3 = Services.objects.get(id=3)
    service4 = Services.objects.get(id=4)
    service5 = Services.objects.get(id=5)
    service6 = Services.objects.get(id=6)
    blog1 = Blog.objects.get(id=1)
    blog2 = Blog.objects.get(id=2)
    blog3 = Blog.objects.get(id=3)
    context = {
        'home': home,
        'about': about,
        'service1': service1,
        'service2': service2,
        'service3': service3,
        'service4': service4,
        'service5': service5,
        'service6': service6,
        'blog1': blog1,
        'blog2': blog2,
        'blog3': blog3,
    }
    return render(request, 'index.html', context)