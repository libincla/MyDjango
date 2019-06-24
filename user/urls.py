from django.urls import path

from . import views

urlpatterns = [
    path('login.html', views.loginView, name='login'),
    path('register.html', views.registerView, name='register'),
    path('setpassword.html', views.setpasswordView, name='setpassword'),
    path('logout.html', views.logoutView, name='logout'),
    path('findpassword.html', views.findPassword, name='findPassword'),
    path('register_new.html', views.registerNewView, name='register_new'),

    # 测试：设置网页的访问权限
    path('weblogin.html', views.webLoginView, name='weblogin'),
    path('webregister.html', views.webRegisterView, name='webregister'),
    path('weblogout.html', views.webLogoutView, name='weblogout'),
]
