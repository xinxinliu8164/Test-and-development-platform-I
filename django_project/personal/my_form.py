from django.forms import ModelForm
from personal.models.manage_project import ManageProject


class ProjectForm(ModelForm):
    class Meta:
        model = ManageProject
        fields = ["name", "describe", "status"]