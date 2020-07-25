from django.shortcuts import render
from .definitions import *
from django.http import JsonResponse
import json
from datetime import datetime

from .models import * # for db saving.

def getMinimums(request):

    p1 = Provider1()
    p2 = Provider2()
    p2Adapter = AnotherProviderAdapter(p2)
    data1 = p1.parseProviderData(p1.getProviderData())
    data2 = p2Adapter.parseProviderData(p2Adapter.getProviderData())
    AllData = [data1,data2]
    result = {}
    for item in AllData:
        for elem in item:
            if elem.name not in result:
                result[elem.name] = elem.value
            elif result[elem.name] > elem.value:
                result[elem.name] = elem.value
    # get current time and save db.

    temp = DBModel(saved_dict = result, time = datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    temp.save()

    return JsonResponse(result)
