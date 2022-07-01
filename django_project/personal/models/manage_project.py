from django.db import models

# Create your models here.


class ManageProject(models.Model):
    """项目"""
    name = models.CharField("项目名称", max_length=100, default='')
    describe = models.CharField("项目描述", max_length=50, default='')
    status = models.BooleanField("项目状态", default=True)
    update_time = models.DateTimeField("更新时间", auto_now=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)

