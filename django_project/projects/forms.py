from django.forms import ModelForm, widgets as wid
from projects.models import ManageProject


class ProjectForm(ModelForm):
    class Meta:
        model = ManageProject
        fields = ["name", "describe", "status"]
        widgets = {"describe": wid.Textarea(attrs={"class": "form-control"})}
