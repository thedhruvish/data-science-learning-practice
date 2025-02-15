from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'index.html')
def show(request):
    return render(request,'show.html')

def myname(request,name):
    return render(request,'myname.html',{'name':name})