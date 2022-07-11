from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def say_hello(requests):
    input_name = requests.GET.get('name', '')
    if not input_name:
        return HttpResponse('请输入一个name')
    return render(requests, 'test.html', {'name': input_name})


def index(requests):
    if requests.method == 'GET':
        return render(requests, 'index.html')
    elif requests.method == "POST":
        username = requests.POST.get('username', '')
        password = requests.POST.get('password', '')
        print('username------->', username)
        print('password------->', password)
        if username is None or password is None:
            error_msg = "用户名或密码不能为空"
            return render(requests, 'index.html', {'error_msg': error_msg})

        user = auth.authenticate(username=username, password=password)
        print('user------->', user)
        if user is None:
            error_msg = "用户名或密码错误"
            return render(requests, 'index.html', {'error_msg': error_msg})
        else:
            auth.login(requests, user)  # 记录登录
            return HttpResponseRedirect('/manage_project/')


@login_required()
def logout(requests):
    auth.logout(requests)
    return render(requests, 'index.html')



@login_required()
def manage_case(requests):
    return render(requests, 'manage_case.html')

