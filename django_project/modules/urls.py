from django.contrib import admin
from django.urls import path
from modules import views

urlpatterns = [
    path('manage_module/', views.manage_module),
    path('manage_module/add_module', views.add_module),
    path('manage_module/edit_module/<int:mid>', views.edit_module),
    path('manage_module/delete_module/<int:mid>', views.delete_module)
]
