from django.shortcuts import render
from chart.models import TotalSales

# 차트페이지 호출
def chlist(request): 
    profit =[19,20,21,22,23,24]
    #profit =[20,15,7,25,27,30]
    qs =  TotalSales.objects.filter(year=2025)
    print(qs)  #  타입 QuerySet list 타입
    print(list(qs.values()))  #타입 list 타입 
    context ={'profit':profit,"list":qs,"list_list":list(qs.values())}
    print(profit)

    return render(request,'chart/chlist.html',context)