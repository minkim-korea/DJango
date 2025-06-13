from django.shortcuts import render
from django.http import JsonResponse #제이슨사용


##하단댓글 등록 
def cwrite(request):
    #html에서 디장고로 데이터전달 
    id=request.POST.get('id')
    cpw=request.POST.get('cpw')
    ccontent=request.POST.get('ccontent')
    print("넘어온데이터:",id,cpw,ccontent)
    context= {'result':'success'}
    return JsonResponse(context)
    




##하단댓글 리스트 -json 타입리턴
def clist(request):
    context= {'result':'success'}
    return JsonResponse(context)
    
