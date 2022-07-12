from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
import json
import requests

# Create your views here.
@login_required()
def manage_case(requests):
    return render(requests, 'manage_case.html')


@login_required()
def debug(request):
    url = request.POST.get("req_url")
    method = request.POST.get("req_method")
    header = request.POST.get("header_editor")
    par_type = request.POST.get("par_type")
    parameters = request.POST.get("parameters")

    header_dict = json.loads(header)
    parameter_dict = json.loads(parameters)


    if method == "get":
        res = requests.request(method=method, url=url, headers=header_dict, params=parameter_dict)
    elif method == "post" and par_type =="json":

        res = requests.request(method=method, url=url, headers=header_dict, json=parameter_dict)
    elif method == "post" and par_type =="form":
        res = requests.request(method=method, url=url, headers=header_dict, data=parameter_dict)



    return JsonResponse(res.text)
