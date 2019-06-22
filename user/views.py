from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password
import random


# Create your views here.

def loginView(request):
    title = '登录'
    unit_2 = '/user/register.html'
    unit_2_name = '立即注册'
    unit_1 = '/user/setpassword.html'
    unit_1_name = '修改密码'
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if User.objects.filter(username=username):
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                return redirect('/')
            else:
                tips = '账号密码错误，请重新输入'
        else:
            tips = '用户不存在，请注册'
    return render(request, 'user.html', locals())


def registerView(request):
    title = '注册'
    unit_2 = '/user/login.html'
    unit_2_name = '立即登录'
    unit_1 = '/user/setpassword.html'
    unit_1_name = '修改密码'
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if User.objects.filter(username=username):
            tips = '用户已存在'
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            tips = '注册成功，请登录'
    return render(request, 'user.html', locals())


def setpasswordView(request):
    title = '修改密码'
    unit_2 = '/user/login.html'
    unit_2_name = '立即登录'
    unit_1 = '/user/register.html'
    unit_1_name = '立即注册'
    new_password = True
    if request.method == 'POST':
        username = request.POST.get('username', '')
        old_password = request.POST.get('password', '')
        new_password = request.POST.get('new_password', '')
        if User.objects.filter(username=username):
            user = authenticate(username=username, password=old_password)
            if user:
                # 使用 set_password 函数修改密码
                user.set_password(new_password)
                user.save()
                tips = '密码修改成功'
                # 使用 make_password 函数修改密码
                dj_ps = make_password(new_password, None, 'pbkdf2_sha256')
                user.password = dj_ps
                user.save()
                tips = '密码修改成功'
            else:
                tips = '原始密码不正确'
        else:
            tips = '用户不存在'
    return render(request, 'user.html', locals())


def logoutView(request):
    logout(request)
    return redirect('/')


def findPassword(request):
    button = '获取验证码'
    new_password = False
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        VerificationCode = request.POST.get('VerificationCode', '')
        user = User.objects.filter(username=username)
        # 用户不存在
        if not user:
            tips = '用户' + username + '不存在'
        else:
            # 判断验证码是否已发送
            if not request.session.get('VerificationCode', ''):
                # 发送验证码并将验证码写入session
                button = '重置密码'
                tips = '验证码已发送'
                new_password = True
                VerificationCode = str(random.randint(1000, 9999))
                request.session['VerificationCode'] = VerificationCode
                # 发送邮件的第一种方式
                user[0].email_user('找回密码', VerificationCode)
            # 匹配输入的验证码是否正确
            elif VerificationCode == request.session.get('VerificationCode'):
                # 密码加密处理并保存到数据库
                dj_ps = make_password(password, None, 'pbkdf2_sha256')
                user[0].password = dj_ps
                user[0].save()
                del request.session['VerificationCode']
                tips = '密码已重置'
            else:
                tips = '验证码错误，请重新输入'
                new_password = False
                del request.session['VerificationCode']
    return render(request, 'findpassword.html', locals())


from django.core.mail import send_mail, send_mass_mail
from django.conf import settings


# 发送邮件的第二种方式
def sendEmailSecondMethod(request):
    from_email = settings.DEFAULT_FROM_EMAIL
    # 发送一封邮件
    # send_mail('MyDjango', 'This is Django', from_email, ['cctvjiatao@163.com'])
    # 发送多封邮件
    message1 = ('MyDjango', 'This is Django', from_email, ['cctvjiatao@163.com'])
    message2 = ('MyDjango', 'This is Django', from_email, ['524sjl@163.com'])
    message3 = ('MyDjango', 'This is Django', from_email, ['jiatao@moyi365.com'])
    send_mass_mail((message1, message2, message3), fail_silently=False)


# 发送邮件的第三种方式
from django.core.mail import EmailMultiAlternatives


def sendEmailThirdMethod(request):
    content = '<p>这是一封<strong>重要的</strong>邮件</p>'
    from_email = settings.DEFAULT_FROM_EMAIL
    msg = EmailMultiAlternatives('MyDjango', content, from_email, ['cctvjiatao@163.com'])
    msg.content_subtype = 'html'
    # 添加附件（可选）
    msg.attach_file('img/p9.jpg')
    msg.send()
