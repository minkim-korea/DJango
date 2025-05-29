from django.shortcuts import render,redirect
from students.models import Student #Student 테이블 연결 
#학생정보 삭제
def delete(request,no):
    Student.objects.get(no=no).delete()
    #return redirect("/students/list/")
    return redirect("students:list") # app_name : path name 찾아서간다.

#학생정보수정페이지열기
def update(request,no):  
    #filter로 해도되는데 리스트타입으로 넘어옴 장점 에러는 안남 
    qs = Student.objects.get(no=no)      #데이터타입 set타입1개 
    context ={"stu":qs}
    # qs = Student.objects.filter(no=no) # 데이터타입: 리스트타입
    # context ={"stu":qs[0]}
    return render(request,'students/update.html',context)
#학생정보수정완료
def updateOk(request):
    no =request.POST.get('no')
    qs = Student.objects.get(no=no) #데이터검색
    # 데이터수정
    qs.name= request.POST.get('name')
    qs.major= request.POST.get('major')
    qs.grade= request.POST.get('grade')
    qs.age=request.POST.get('age')
    qs.gender=request.POST.get('gender')
    hobby =request.POST.getlist('hobby')
    hobby=','.join(hobby)
    qs.hobby= hobby    
    qs.save()
    
    return redirect(f'/students/view/{no}/')



#학생정보 상세보기
def view(request,no):
    try:
      qs = Student.objects.get(no=no)
    except:
        qs = None 
    print('전달 no: ',no)
    context = {'stu':qs}
    return render(request,"students/view.html",context)




#학생정보저장 
def writeOk(request):
    # 학생정보저장 
    name = request.POST.get('name')
    major= request.POST.get('major')
     #major= request.POST['major']
    grade = request.POST.get('grade')
    age= request.POST.get('age')
    gender= request.POST.get('gender')
    #취미 여러개 리스트형태로 
    hobby= request.POST.getlist('hobby')
    # 리스트타입을 -> str타입으로 변경해줘야됨 
    hobby =','.join(hobby)  # 'game,golf,swim'

    print("저장정보 이름:",name)
    print("저장정보 학과:",major)
    print("저장정보 hobby:",hobby)  #['game','golf','swim']
    Student(name=name,major=major,grade=grade,age=age,gender=gender,hobby=hobby,memo="등록합니다.").save()
    return redirect('/students/list/')

#학생정보등록페이지 열기 (저장아님)
def write(request):
    # if request.method =="GET":
    return render(request,'students/write.html')
    # else : # if request.method == 'POST':
    #     return redirect('/students/list/')


#학생정보리스트
def list(request):
    qs = Student.objects.all()
    context = {'list':qs}
    #render 폴더앞에는 / 안붙임. 
    return render(request,"students/list.html",context)




