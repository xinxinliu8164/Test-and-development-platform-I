from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from personal.models.manage_project import ManageProject
from personal.my_form import ProjectForm


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


@login_required()  # 可保证manage页面只有登录成功的用户才能访问，退出的用户user将被删除，无法访问
def manage_project(requests):
    projects = ManageProject.objects.all()
    return render(requests, 'manage_project.html', {"projects": projects, "type": "projects_list"})


@login_required()
def add_project(requests):
    if requests.method == 'GET':
        projects = ManageProject.objects.all()
        return render(requests, 'manage_project.html', {"projects": projects, "type": "add_project"})
    elif requests.method == "POST":
        project_name = requests.POST.get("project_name")
        project_describe = requests.POST.get("project_describe")
        status = requests.POST.get("status")
        p = ManageProject.objects.create(name=project_name, describe=project_describe, status=status)
        projects = ManageProject.objects.all()
    return render(requests, 'manage_project.html', {"projects": projects, "type": "projects_list"})


@login_required()
def edit_project(requests, pid):
    if requests.method == 'GET':
        project = ManageProject.objects.get(id=pid)
        form = ProjectForm(instance=project)
        return render(requests, f'manage_project.html', {"form": form, "pid": pid, "type": "edit_project"})
    elif requests.method == "POST":
        form = ProjectForm(requests.POST)
        if form.is_valid():
            project = ManageProject.objects.get(id=pid)
            project.name = form.cleaned_data['name']
            project.describe = form.cleaned_data['describe']
            project.status = form.cleaned_data['status']
            project.save()
        projects = ManageProject.objects.all()
        return render(requests, 'manage_project.html', {"projects": projects, "type": "projects_list"})


@login_required()
def manage_module(requests):
    return render(requests, 'manage_module.html')


@login_required()
def manage_case(requests):
    return render(requests, 'manage_case.html')

