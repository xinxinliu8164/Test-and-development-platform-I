from django.db import models

# Create your models here.


class ManageProject(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    create_time = models.TimeField(auto_now_add=True)