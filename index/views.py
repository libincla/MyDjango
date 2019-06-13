from django.shortcuts import render


def index(request):
    return render(request, 'index.html', context={'title': '首页'}, status=500)
