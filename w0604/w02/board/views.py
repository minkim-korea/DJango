from django.shortcuts import render,redirect
from board.models import Board
from django.db.models import F 

def list(request):
    qs =Board.objects.order_by("-bgroup","bstep")
    context={"list":qs}
    return render(request,"board/list.html",context)

def write(request):
    if request.method == "GET":
        return render(request,'board/write.html')
    elif request.method == "POST":
        # 데이터 가져오기
        id = request.POST.get('id') #섹션에서 가져옴.
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        print('write 가져온 데이터 : ',id,btitle,bcontent,bfile)
        # 1.save() 저장
        # Board(id=id,btitle=btitle,bcontent=bcontent,bfile=bfile).save()
        # 2.create저장
        qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent,bfile=bfile)
        qs.bgroup = qs.bno
        qs.save()
        context = {'msg':1}
        return render(request,'board/write.html',context)
    
def view(request,bno):
    qs = Board.objects.filter(bno=bno) # 리스트
    qs.update(bhit = F('bhit')+1) #save까지 됨.
    context = {'board':qs[0]}
    return render(request,'board/view.html',context)

def update(request,bno):
        if request.method == 'GET':
            qs = Board.objects.get(bno=bno)
            context = {'board':qs}
            return render(request,'board/update.html',context)
        elif request.method == 'POST':
            btitle = request.POST.get('btitle')
            bcontent = request.POST.get('bcontent')
            bfile = request.POST.get('bfile')
            qs = Board.objects.get(bno=bno)
            qs.btitle = btitle
            qs.bcontent = bcontent
            # qs.bfile = bfile
            qs.save()
            context = {'msg':1,'board':qs}
            return render(request,'board/update.html',context)
        
def delete(request,bno):
    Board.objects.get(bno=bno).delete()    
    return redirect('/board/list/')

def reply(request,bno):
    if request.method == 'GET':
        qs = Board.objects.get(bno=bno)
        context = {'board':qs}
        return render(request,'board/reply.html',context)
    elif request.method == 'POST':
        id = request.POST.get("id")
        bgroup = request.POST.get("bgroup") 
        bstep = int(request.POST.get("bstep"))
        bindent = int(request.POST.get("bindent")) 
        btitle = request.POST.get("btitle")
        bcontent = request.POST.get("bcontent")
        bfile = request.POST.get("bfile")
        reply_qs = Board.objects.filter(bgroup=bgroup,bstep__gt=bstep)
        reply_qs.update(bstep = F('bstep')+1)
        # db저장
        qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent,
            bgroup=bgroup,bstep=bstep+1,bindent=bindent+1,bfile=bfile)
        print('')        
        context = {"msg":1,'board':qs}
        return render(request,'board/reply.html',context)