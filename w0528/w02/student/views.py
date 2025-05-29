from django.shortcuts import render,redirect
from student.models import Student
# from django.http import HttpResponseRedirect
#학생정보 삭제

def delete(request,name):
    #검색
    print("삭제이름:",name)
    qs = Student.objects.get(name=name)
    qs.delete() 
    return redirect("/student/list")

 #학생정보 수정   
def update(request,name):
    if request.method =='POST' :
         name2= request.POST.get("name")
         major= request.POST.get("major")
         grade= request.POST.get("grade")
         age= request.POST.get("age")
         gender= request.POST.get("gender")
         print("입력된 정보 :" ,name,major,grade,age,gender)
         #db수정 1.회원검색
         qs = Student.objects.get(name=name)
         #2.회원정보수정 
         qs.name = name2
         qs.major =major
         qs.grade= grade
         qs.age= age
         qs.gender=gender
         qs.save()
         print("Student 객체 수정")
         return redirect("/student/list/")
       
    else:  
        print("학생이름:",name)
        qs = Student.objects.get(name=name)
        context = {'stu':qs}
        return render (request,"student/update.html",context)
        
   
#학생정보 상세보기 
def view(request):
    name = request.GET.get("name")
    qs = Student.objects.get(name=name)
    context = {'stu':qs}
    print("전달 이름 : ",name)
    return render(request,'student/view.html',context)



#학생정보 등록
def write(request):
    if  request.method =='POST': # POST방식으로 들어올때 정보를 db저장
        name= request.POST.get("name")
        major= request.POST.get("major")
        grade= request.POST.get("grade")
        age= request.POST.get("age")
        gender= request.POST.get("gender")
        print("입력된 정보 :" ,name,major,grade,age,gender)
        Student(name=name,major=major,grade=grade,age=age,gender=gender).save()
        print("Student 객체 저장")
        return redirect("/student/list/")
    
    else: # get방식으로 들어올때
       print("request method:",request.method)
       return render(request,"student/write.html")
   
#학생정보리스트
def list(request):
     #db검색 - objects.all():전체 가져오기 ,object.get()해당되는것가져오기
     # objects.filter(): 검색기능 - __contains, gte크거나같다,gt 크다 ,lt 작다 lte:작거나같다
     # objects.order.by() : 정렬 
       #qs=Student.objects.all()
       #qs=Student.objects.order_by()# 순차정렬
       qs=Student.objects.order_by('-id') # 순차정렬 -는역순 
       #딕셔너리 타입으로 전달 
       #context={'list':qs,'count':100,"id":"aaa"}
       context={'list':qs}
       return render(request,"student/list.html",context)
   
#  #학생정보 수정   
# def update(request,name):
#     if request.method =='GET' :
#         print("학생이름:",name)
#         qs = Student.objects.get(name=name)
#         context = {'stu':qs}
#         return render (request,"student/update.html",context)
#     else:  
        
#          name2= request.POST.get("name")
#          major= request.POST.get("major")
#          grade= request.POST.get("grade")
#          age= request.POST.get("age")
#          gender= request.POST.get("gender")
#          print("입력된 정보 :" ,name,major,grade,age,gender)
#          #db수정 1.회원검색
#          qs = Student.objects.get(name=name)
#          #2.회원정보수정 
#          qs.name = name2
#          qs.major =major
#          qs.grade= grade
#          qs.age= age
#          qs.gender=gender
#          qs.save()
#          print("Student 객체 수정")
#          return redirect("/student/list/")