from django.shortcuts import render

def write(request):
    return render(request,'students/write.html')

def result(request):
    # post방식 - name,kor,eng,hobby
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    hobbys = request.POST.getlist('hobby')
   
    context = {"id":id,"pw":pw,"name":name,"gender":gender,"hobby":hobbys}
    return render(request,'students/result.html',context)
