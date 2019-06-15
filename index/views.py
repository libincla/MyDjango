from django.shortcuts import render, redirect
from .models import Product


def index(request):
    type_list = Product.objects.values('type').distinct()
    name_list = Product.objects.values('name', 'type')
    title = '首页'
    return render(request, 'index.html', context=locals(), status=200)


def login(request):
    # 相对路径
    return redirect('/')
    # 绝对路径
    # return redirect('http://127.0.0.1:8000/')
