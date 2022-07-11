from django.forms import ModelForm, widgets as wid
from modules.models import ManageModule


class ModuleForm(ModelForm):
    class Meta:
        model = ManageModule
        fields = ['project', 'name', 'desc']
        widgets = {"desc": wid.Textarea(attrs={"class": "form-control"})}