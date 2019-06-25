from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login.html', views.login),
    path('index/', views.ProductList.as_view()),
    path('index/<id>.html', views.ProductListWithArgs.as_view(), {'name': 'phone'}),
    path('index/data_form', views.index_form, name='data_form'),
    path('index/data_model_form/<int:id>.html', views.index_model_form, name='data_model_form'),
    path('shopping_car.html', views.ShoppingCarView, name='ShoppingCar'),
]
