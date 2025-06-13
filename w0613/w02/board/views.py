from django.shortcuts import render





#뷰페이지연결  
def notice_view(request):
    return render(request,"board/notice_view.html")




## 게시판리스트
def notice(request):
    # db에서 가져오기
 return render(request,"board/notice.html")