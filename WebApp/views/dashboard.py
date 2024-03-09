from django.shortcuts import render
from django.http import HttpResponse

def dashboard_view(request):
    print('yes function is working')
    print('ankit')
    return render(request,'dashboard.html')
