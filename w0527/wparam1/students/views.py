from django.shortcuts import render



def list(request):
    #get방식으로
    name = request.GET.get('name')
    age = request.GET.get('age')
    print("이름 : ",name)
    print("나이 : ",age)
    context={"name":name ,"age":age}
    return render(request,"list.html",context)
    