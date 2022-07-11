from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from modules.models import ManageModule
from projects.models import ManageProject
from modules.forms import ModuleForm
# Create your views here.


@login_required()
def manage_module(requests):
    modules = ManageModule.objects.all()
    return render(requests, 'manage_module.html', {"modules": modules, "type": "module_list"})


@login_required()
def add_module(requests):
    if requests.method == 'GET':
        projects = ManageProject.objects.all()
        #print(json.dumps(projects, indent=2,ensure_ascii=False))
        modules = ManageModule.objects.all()
        return render(requests, 'manage_module.html', {"modules": modules, "projects": projects, "type": "add_module"})
    elif requests.method == "POST":
        project_id = requests.POST.get("project")
        print("------->>>>", project_id)
        # project = ManageProject.objects.filter(name=module_project_name)[0]
        module_name = requests.POST.get("module_name")
        module_describe = requests.POST.get("module_describe")
        ManageModule.objects.create(name=module_name, desc=module_describe, project_id=project_id)
        return HttpResponseRedirect('/manage_module/')


@login_required()
def edit_module(requests, mid):
    if requests.method == 'GET':
        module = ManageModule.objects.get(id=mid)
        form = ModuleForm(instance=module)
        print("****", form)
        return render(requests, f'manage_module.html', {"form": form, "type": "edit_module"})
    elif requests.method == "POST":
        form = ModuleForm(requests.POST)
        if form.is_valid():
            module = ManageModule.objects.get(id=mid)
            # module.project =
            module.name = form.cleaned_data['name']
            module.desc = form.cleaned_data['desc']
            module.save()
        return HttpResponseRedirect('/manage_module/')


@login_required()
def delete_module(requests, mid):
    if requests.method == "GET":
        module = ManageModule.objects.get(id=mid)
        module.delete()
    return HttpResponseRedirect('/manage_module/')

