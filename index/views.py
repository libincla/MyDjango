from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product, Type
from django.views.generic import ListView
from .form import *
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required(login_url='/user/weblogin.html')
@permission_required(perm='index.visit_Product', login_url='/user/weblogin.html')
def index(request):
    product = request.GET.get('product', '')
    price = request.GET.get('price', '')
    if product:
        product_list = request.session.get('product_info', [])
        if product not in product_list:
            product_list.append({'price': price, 'product': product})
        request.session['product_info'] = product_list
        return redirect('/')
    return render(request, 'index.html', locals())


# 使用装饰器 login_required 和 permission_required 分别对用户登录验证和用户权限验证
# @login_required(login_url='/user/weblogin.html')
# @permission_required(perm='index.visit_Product', login_url='/user/weblogin.html')
# def index(request):
#     return render(request, 'index.html', context=locals())


# 使用 has_perm 实现装饰器 permission_required 功能
# @login_required(login_url='/user/weblogin.html')
# def index(request):
#     user = request.user
#     if user.has_perm('index.visit_Product'):
#         return render(request, 'index.html', context=locals())
#     else:
#         return redirect('/user/weblogin.html')


# def index(request):
#     type_list = Type.objects.values('id', 'type_name')
#     name_list = Product.objects.values('name', 'type')
#     title = '首页'
#     username = request.user.username
#     return render(request, 'index.html', context=locals())


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


def index_form(request):
    if request.method == 'GET':
        product = ProductForm()
        return render(request, 'data_form.html', locals())
    else:
        product = ProductForm(request.POST)
        if product.is_valid():
            name = product['name']
            # 将控件 name 的数据进行清洗，转换成 Python 数据类型
            cname = product.cleaned_data['name']
            return HttpResponse('提交成功')
        else:
            error_msg = product.errors.as_json()
            print(error_msg)
            return render(request, 'data_form.html', locals())


# http://127.0.0.1:8000/index/data_model_form/2.html
def index_model_form(request, id):
    if request.method == 'GET':
        # 初始化方法1
        # product = ProductModelForm(initial={'name': '华为手表'})

        # 初始化方法2
        # instance = Product.objects.filter(id=id)
        # if instance:
        #     product = ProductModelForm(instance=instance[0])
        # else:
        #     product = ProductModelForm()

        # 初始化方法4:重写ProductModelForm类的初始函数 __init__，详见ProductModelForm类
        product = ProductModelForm()

        return render(request, 'data_form.html', locals())
    else:
        product = ProductModelForm(request.POST)
        if product.is_valid():
            weight = product.cleaned_data['weight']
            product_db = product.save(commit=False)
            product_db.name = '我的iPhone'
            product_db.save()
            return HttpResponse('提交成功! weight清洗后的数据为：' + weight)
        else:
            error_msg = product.errors.as_json()
            print(error_msg)
            return render(request, 'data_form.html', locals())


@login_required(login_url='/user/weblogin.html')
def ShoppingCarView(request):
    product_list = request.session.get('product_info', [])
    del_product = request.GET.get('product', '')
    if del_product:
        for i in product_list:
            if i['product'] == del_product:
                product_list.remove(i)
        request.session['product_info'] = product_list
        return redirect('/shopping_car.html')
    return render(request, 'shopping_car.html', locals())


def messageView(request):
    # 信息添加方法1
    messages.info(request, '提示信息')
    messages.success(request, '提示正确')
    messages.warning(request, '提示警告')
    messages.error(request, '提示错误')
    # 信息添加方法2
    messages.add_message(request, messages.INFO, '信息提示')
    return render(request, 'message.html', locals(), RequestContext(request))


def paginationView(request, page):
    Product_list = Product.objects.all()
    # 设置每一页的数据量为3
    paginator = Paginator(Product_list, 3)
    try:
        pageInfo = paginator.page(page)
    except PageNotAnInteger:  # 如果参数page的数据类型不是整形，就返回第一页数据
        pageInfo = paginator.page(1)
    except EmptyPage:  # 如果要访问的页数大于实际页数，就返回最后一页的数据
        pageInfo = paginator.page(paginator.num_pages)
    return render(request, 'pagination.html', locals())
