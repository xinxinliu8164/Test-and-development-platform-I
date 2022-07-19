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
    # 用例列表
    path('manage_case/', views.manage_case),

    # 添加用例
    path('manage_case/case_add', views.case_add),
    path('manage_case/case_add/debug', views.debug),
    path('manage_case/case_add/case_assert', views.case_assert),
    path('manage_case/case_add/get_select_data', views.get_select_data),
    path('manage_case/case_add/save_case', views.save_case),

    # 用例编辑
    path('manage_case/case_edit/<int:cid>', views.case_edit),

    # 用例删除
    path('manage_case/case_delete/<int:cid>', views.case_delete)
]