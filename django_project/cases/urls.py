# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2022/7/12 下午4:35 
  @Auth : 波子汽水味儿的满天星
  @File : urls.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1252919904@qq.com
  @Company: test
-------------------------------------------------
"""

from django.contrib import admin
from django.urls import path
from cases import views

urlpatterns = [
    path('manage_case/', views.manage_case),
    path('manage_case/debug', views.debug),
    path('manage_case/case_assert', views.case_assert),
    path('manage_case/get_select_data', views.get_select_data),
    path('manage_case/save_case', views.save_case)
]