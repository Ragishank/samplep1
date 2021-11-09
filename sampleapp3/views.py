from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fnHome(request):
    return HttpResponse("hii i am ragisha")
def fnLogin(request):
    return render(request,'login.html')
