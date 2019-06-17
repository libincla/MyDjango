from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product, Type
from django.views.generic import ListView


def index(request):
    type_list = Type.objects.values('id', 'type_name')
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


# http://127.0.0.1:8000/index
class ProductList(ListView):
    # 设置 HTML 模板的变量名称
    context_object_name = 'type_list'

    # 设定模板名称
    template_name = 'index.html'

    # 查询数据，查询结果会赋值给 context_object_name所设置的变量
    queryset = Product.objects.values('type').distinct()

    # 重写函数 get_queryset，该函数的功能与 queryset实现的功能一致
    # def get_queryset(self):
    #     type_list = Product.objects.values('type').distinct()
    #     return type_list

    # 添加其他变量
    # 重写函数 get_context_data，该函数设置 HTML 模板的其他变量
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name_list'] = Product.objects.values('name', 'type')
        return context


# http://127.0.0.1:8000/index/2.html
class ProductListWithArgs(ListView):
    # 设置 HTML 模板的变量名称
    context_object_name = 'type_list'
    # 设定模板名称
    template_name = 'index.html'

    # 重写查询函数 get_queryset，查询结果会赋值给 context_object_name所设置的变量
    def get_queryset(self):
        print(self.kwargs['id'])
        print(self.kwargs['name'])
        print(self.request.method)
        type_list = Product.objects.values('type').distinct()
        return type_list

    # 添加其他变量
    # 重写函数 get_context_data，该函数设置 HTML 模板的其他变量
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name_list'] = Product.objects.values('name', 'type')
        return context
