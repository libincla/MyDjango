from django.urls import path

from . import views

urlpatterns = [
    path('login.html', views.loginView, name='login'),
    path('register.html', views.registerView, name='register'),
    path('setpassword.html', views.setpasswordView, name='setpassword'),
    path('logout.html', views.logoutView, name='logout'),
    path('findpassword.html', views.findPassword, name='findPassword'),
    path('register_new.html', views.registerNewView, name='register_new'),
]
