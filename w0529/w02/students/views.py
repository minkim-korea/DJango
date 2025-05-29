from django.shortcuts import render,redirect
from students.models import Student
#뷰 
def view(request,no):
    try:
      qs = Student.objects.get(no=no)
    except:
        qs = None 
    context = {'stu':qs}
    return render(request,"students/view.html",context)





#삭제
def delete(request,no):
    Student.objects.get(no=no).delete()
    return redirect("students:list")
   
#업데이트
def update(request,no): 
    # qs = Student.objects.get(no=no)    
    # context ={"stu":qs}
    qs = Student.objects.filter(no=no) # 데이터타입: 리스트타입
    context ={"stu":qs[0]}
    return render(request,'students/update.html',context)
def updateOk(request):
    no =request.POST.get('no')
    qs = Student.objects.get(no=no) #데이터검색
    qs.name= request.POST.get('name')
    qs.major= request.POST.get('major')
    qs.grade= request.POST.get('grade')
    qs.age=request.POST.get('age')
    qs.gender=request.POST.get('gender')
    hobby =request.POST.getlist('hobby')
    hobby=','.join(hobby)
    qs.hobby= hobby    
    qs.save()
    return redirect('/students/list/')
#리스트
def list(request):
    qs = Student.objects.all()
    context = {'list':qs}
    return render(request,"students/list.html",context)
# 라이트 
def write(request):
    return render(request,"students/write.html")
def writeOk(request):
    name = request.POST.get('name')
    major= request.POST.get('major')
    grade = request.POST.get('grade')
    age= request.POST.get('age')
    gender= request.POST.get('gender')
    hobby= request.POST.getlist('hobby')
    hobby =','.join(hobby)
    Student(name=name,major=major,grade=grade,age=age,gender=gender,hobby=hobby).save()
    return redirect('/students/list/')

