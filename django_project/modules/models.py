from django.db import models

# Create your models here.
from projects.models import ManageProject


class ManageModule(models.Model):
    """模块"""
    project = models.ForeignKey(ManageProject, on_delete=models.CASCADE)
    name = models.CharField("模块名称", max_length=100, default='')
    desc = models.CharField("模块描述", max_length=50, default='')
    update_time = models.DateTimeField("更新时间", auto_now=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)

    def __str__(self):
        # return u'{0}'.format(self.name)
        return self.name