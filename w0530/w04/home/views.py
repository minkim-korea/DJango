from django.shortcuts import render

def index(request):
    cook_info = request.COOKIES #모든쿠키정보 가져오기 
    test_id =request.COOKIES.get("test","") # 쿠키 정보1개 읽기 
    print("쿠키정보 : ", cook_info)
    context = {"cook_info":cook_info}
    response = render(request,"index.html",context)
    if test_id =="": 
       
        response.set_cookie("test","aaa",max_age=60*60*24*365) #쿠키1개저장
        print("test쿠키저장")
    else:
        response.delete_cookie('test') # 쿠키삭제 
        print("test쿠키삭제")
    return response
