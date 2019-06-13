from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello world")


# http://127.0.0.1:8000/2019/06/13
def mydate(request, year, month, day):
    return HttpResponse(str(year) + '/' + str(month) + '/' + str(day))


# http://127.0.0.1:8000/2019/06/14.html
def re_mydate(request, year, month, day):
    return HttpResponse(str(year) + '/' + str(month) + '/' + str(day))


# http://127.0.0.1:8000/2012.html
def myyear(request, year):
    return render(request, 'myyear.html')


# http://127.0.0.1:8000/dict/2012.htm
def myyear_dict(request, year, month):
    return render(request, 'myyear_dict.html', {'month': month})
