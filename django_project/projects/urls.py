from django.contrib import admin
from django.urls import path
from projects import views


urlpatterns = [
    path('manage_project/', views.manage_project),
    path('manage_project/add_project', views.add_project),
    path('manage_project/edit_project/<int:pid>', views.edit_project),
    path('manage_project/delete_project/<int:pid>', views.delete_project)

]
