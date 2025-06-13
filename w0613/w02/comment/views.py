from django.shortcuts import render
from django.http import JsonResponse





def clist(request):
    context = {'result':'success'}
    return JsonResponse(context)
