from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def miten(requser):
    return render(requser, 'index.html')

def two(requser):
    return HttpResponse("<h1>hello</h1>")
