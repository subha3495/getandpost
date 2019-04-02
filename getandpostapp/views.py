from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def getinput(request):
    return render(request,'getinput.html')
def postinput(request):
    return render(request,'postinput.html')
def add(request):
    if request.method == "GET":
        try:
            a=request.GET['t1']
            x=int(a)
            b=request.GET['t2']
            y=int(b)
            z=x+y
            return HttpResponse("<html><body bgcolor=cyan><h1>sum is:"+str(z)+"</h1></body></html>")
        except(ValueError):
            return  HttpResponse("Invalid input")
    else:
        try:
            a=request.POST['t1']
            x=int(a)
            b=request.POST['t2']
            y=int(b)
            z=x+y
            return HttpResponse("<html><body bgcolor=cyan><h1>sum is:"+str(z)+"</h1></body></html>")
        except(ValueError):
            return  HttpResponse("Invalid input")

