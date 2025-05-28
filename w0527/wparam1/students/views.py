from django.shortcuts import render



def list(request):
    #get방식으로
    name = request.GET.get('name')
    age = request.GET.get('age')
    print("이름 : ",name)
    print("나이 : ",age)
    context={"name":name ,"age":age}
    return render(request,"list.html",context)
    
    
def result(request):
    #get방식으로
    id = request.GET.get('id')
    pw = request.GET.get('pw')
    name = request.GET.get('name')
    print("아이디 : ",id)
    print("pw : ",pw)
    print("이름 : ",name)
    context={ "id":id,"pw":pw,"name":name}
    return render(request,"result.html",context)




    
   
