from django.shortcuts import render
def write(request):
    return render(request,"students/write.html")

def result(request):
    name =request.POST.get("name")
    kor = request.POST.get('kor')
    eng = request.POST.get('eng')
    total=int(kor)+int(eng)  #타입변경해서 합계를 구한다. 
    hobbys = request.POST.getlist("hobby") #리스트
    print("이름 : ",name)
    context={"name":name ,"kor":kor ,"eng":eng , "hobby":hobbys,"total":total}
    return render(request,"students/result.html",context)

def send(request,name,age,):
    print('전달받은값 :',name,age)
    
    context={"name":name ,"age":age}
    return render(request,"students/send.html",context)
    




def view(request):
    #get방식으로
    name = request.GET.get('name')
    age = request.GET.get('age')
    print("이름 : ",name)
    print("나이 : ",age)
    context={"name":name ,"age":age}
    return render(request,"students/view.html",context)


def list (request):
    
    
    # request -> id=aaa
    id = request.POST.get("id") #변수
    pw = request.POST.get("pw")#변수
    gender = request.POST.get("gender")#변수
    hobbys = request.POST.getlist("hobby") #리스트
    tel = request.POST.get("tel")    #변수
    print("입력된 id값 :",('id'))
    print("입력된 pw값 :",('pw'))
    print("입력된 성별  :",gender)
    print("입력된 취미 :",hobbys)
    print("입력된 전화번호 :",('tel'))
   
    context ={"id":id,"pw":pw , "gender":gender ,"tel":tel,"hobby":hobbys }
    return render(request,"students/list.html",context)

