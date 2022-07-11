from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from projects.models import ManageProject
from projects.forms import ProjectForm


# Create your views here.
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
        return HttpResponseRedirect('/manage_project/')


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
            print(project.name)
        return HttpResponseRedirect('/manage_project/')


@login_required()
def delete_project(requests, pid):
    if requests.method == "GET":
        project = ManageProject.objects.get(id=pid)
        project.delete()
    return HttpResponseRedirect('/manage_project/')
