from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product


def index(request):
    type_list = Product.objects.values('type').distinct()
    name_list = Product.objects.values('name', 'type')
    title = '首页'
    return render(request, 'index.html', context=locals(), status=200)


# http://127.0.0.1:8000/login.html
# http://127.0.0.1:8000/login.html?name=Tom
def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        return redirect('/')
    else:
        if request.GET.get('name'):
            name = request.GET.get('name')
        else:
            name = 'Everyone'
        return HttpResponse('username is ' + name)
