from django.forms import ModelForm, widgets as wid
from personal.models.manage_project import ManageProject
from personal.models.manage_module import ManageModule



class ProjectForm(ModelForm):
    class Meta:
        model = ManageProject
        fields = ["name", "describe", "status"]
        widgets = {"describe": wid.Textarea(attrs={"class":"form-control"})}



class ModuleForm(ModelForm):
    class Meta:
        model = ManageModule
        fields = ['project', 'name', 'desc']
        widgets = {"desc": wid.Textarea(attrs={"class":"form-control"})}


