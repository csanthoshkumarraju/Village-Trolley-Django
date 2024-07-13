from django.shortcuts import render
from django.http import HttpResponse
 
def home(request):
    return render(request, 'home.html')
    
def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def additems(request):
    return render(request, 'additems.html')

def billingform(request):
    return render(request,'billingform.html')

def analytics(request):
    return render(request,'analytics.html')


def lowstock(request):
    return render(request,'lowstockproducts.html')

def nearbystores(request):
    return render(request,'nearbystores.html')

def shopproducts(request):
    return render(request,'shopdetails.html')

def knowmore(request):
    return render(request,'knowmore.html')

def daily_monthly_data(request):
    return render(request,'dailymonthlydata.html')

def resetpwd(request):
    return render(request,'resetpassword.html')

def custdmhist(request):
    return render(request,'customerdailymonthlydata.html')