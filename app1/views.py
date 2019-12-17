from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello Shekhar</h1>')


def home2(request):
    print('hELLO')
    list = [1,2,3,4,5,6,'SHEKHAR']
    return render(request,'app1/home2.html',context={'list':list})

def m1(request):
    di={1:'Shekhar',2:'Ravi',3:'Shailesh',4:'Ranjitsinh'}
    return render(request,'app1/home2.html',{'di':di})
