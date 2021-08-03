from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def change(request):
    t=request.POST.get('text','default')
    d=request.POST.get('day','default')
    top = request.POST.get('topic','default')
    if t=='':
        return render(request,'fillit.html')

    return render(request, 'change.html',{'text':t,'day':d,'topic':top})