from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
import json
import requests
from projects.models import ManageProject


# Create your views here.
@login_required()
def manage_case(request):
    projects = ManageProject.objects.all()
    return render(request, 'manage_case.html', {"projects": projects})


@login_required()
def debug(request):
    global res
    url = request.POST.get("req_url")
    method = request.POST.get("req_method")

    header = request.POST.get("header_editor")
    header = header.replace("\'", "\"")

    par_type = request.POST.get("par_type")

    parameters = request.POST.get("parameters")
    parameters = parameters.replace("\'", "\"")

    print(method)
    print(par_type)

    if header:
        header_dict = json.loads(header)
    if parameters:
        parameter_dict = json.loads(parameters)

    if not parameters and not header:
        res = requests.request(method=method, url=url)

    if method == "get":
        if header and parameters:
            res = requests.request(method=method, url=url, headers=header_dict, params=parameter_dict)
        elif parameters and not header:
            res = requests.request(method=method, url=url, params=parameter_dict)

    elif method == "post" and par_type == "json":
        if header and parameters:
            res = requests.request(method=method, url=url, headers=header_dict, json=parameter_dict)
        elif parameters and not header:
            res = requests.request(method=method, url=url, json=parameter_dict)

    elif method == "post" and par_type == "form":
        if header and parameters:
            res = requests.request(method=method, url=url, headers=header_dict, data=parameter_dict)
        elif parameters and not header:
            res = requests.request(method=method, url=url, data=parameter_dict)
    return JsonResponse({"result": res.text})


@login_required()
def case_assert(request):
    actual_result = request.POST.get("actual_result")
    expect_result = request.POST.get("expect_result")
    assert_type = request.POST.get("assert_type")

    print(actual_result)
    print(expect_result)
    print(assert_type)

    if assert_type == 'contains':
        if expect_result in actual_result:
            return JsonResponse({"result": "断言成功"})
        else:
            return JsonResponse({"result": "断言失败"})
    elif assert_type == "equal":
        if expect_result == actual_result:
            return JsonResponse({"result": "断言成功"})
        else:
            return JsonResponse({"result": "断言失败"})
