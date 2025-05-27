from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from students.models import Student
from django.urls import reverse 
# Create your views here.
def list(request):
    #Student테이블 데이터 가져오기 
    qs = Student.objects.all()
    context = {"list":qs}
    return render(request,'list.html',context)

#학생등록페이지
def write(request):
    return render(request,"write.html")

#학생등록저장
def write2(request):
    # request.POST[], request.POST.get()
    name = request.POST.get('name')
    major = request.POST.get('major')
    grade = request.POST.get('grade')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    print("데이터정보:",name,major,grade,age,gender)
    qs = Student(name=name,major=major,grade=grade,age=age,gender=gender)
    qs.save()
    return redirect("students:list")
    # 앱이름으로 링크 , url 링크 
    #return redirect("/students/list")
      # return HttpResponseRedirect(reverse('students:list'))
      # render(request,"write.html") # students/write




    # txt = '''
    # <html>
    
    # <head>
    # </head>
    # <body>
    # <h2>학생리스트 페이지 </h2>
    # </body>
    # </html>
    
    
    # '''
    # return HttpResponse(txt)