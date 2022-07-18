from django.contrib import admin

# Register your models here.
from cases.models import TestCase


admin.site.register(TestCase)