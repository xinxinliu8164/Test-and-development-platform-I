from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
import json
import requests

from modules.models import ManageModule
from projects.models import ManageProject
from cases.models import TestCase


# Create your views here.
@login_required()
def manage_case(request):
    cases = TestCase.objects.all()
    return render(request, 'manage_case.html', {"cases": cases})



@login_required()
def case_edit(request):
    pass


@login_required()
def case_delete(request):
    pass


@login_required()
def case_add(request):
    return render(request, 'case_add.html')


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
            return JsonResponse({"result": "????????????"})
        else:
            return JsonResponse({"result": "????????????"})
    elif assert_type == "equal":
        if expect_result == actual_result:
            return JsonResponse({"result": "????????????"})
        else:
            return JsonResponse({"result": "????????????"})


def get_select_data(request):
    """??????????????????"""
    if request.method == "GET":
        projects = ManageProject.objects.all()
        data_list = []
        for i in projects:
            project_info = {
                "id": i.id,
                "name": i.name
            }

            modules = ManageModule.objects.filter(project_id=i.id)
            module_list = []
            for j in modules:
                module_info = {
                    "id": j.id,
                    "name": j.name
                }
                module_list.append(module_info)

            project_info.setdefault("module_list", module_list)

            data_list.append(project_info)

        return JsonResponse({"status": "10200", "msg": "success", "data": data_list})
    else:
        return JsonResponse({"status": "10500", "msg": "??????????????????"})


@login_required()
def save_case(request):
    if request.method == "POST":
        case_name = request.POST.get("case_name")
        module_id = request.POST.get("module_id")

        url = request.POST.get("url")
        req_method = request.POST.get("req_method")
        header_editor = request.POST.get("header_editor")
        par_type = request.POST.get("par_type")
        parameters = request.POST.get("parameters")
        rep_result = request.POST.get("rep_result")

        assert_type = request.POST.get("assert_type")
        assert_text = request.POST.get("assert_text")

        if case_name == '':
            return JsonResponse({"status": "10500", "msg": "??????????????????"})
        elif module_id == '':
            return JsonResponse({"status": "10500", "msg": "??????????????????"})
        elif url == "":
            return JsonResponse({"status": "10500", "msg": "????????????url??????"})
        elif req_method == '':
            return JsonResponse({"status": "10500", "msg": "????????????????????????"})
        else:
            print('======>', case_name)

            case = TestCase.objects.create(name=case_name, module_id=module_id,
                                    url=url, req_method=req_method, header_editor=header_editor,
                                    par_type=par_type, parameters=parameters, rep_result=rep_result,
                                    assert_type=assert_type, assert_text=assert_text)
            print('---->', case.name)
            return JsonResponse({"status": "10200", "msg": "??????????????????"})


