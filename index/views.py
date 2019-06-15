from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html', context={'title': '首页'}, status=500)


def login(request):
    # 相对路径
    return redirect('/')
    # 绝对路径
    # return redirect('http://127.0.0.1:8000/')
