from django.forms import ModelForm, widgets as wid
from personal.models.manage_project import ManageProject



class ProjectForm(ModelForm):
    class Meta:
        model = ManageProject
        fields = ["name", "describe", "status"]
        widgets = {"describe": wid.Textarea(attrs={"class":"form-control"})}