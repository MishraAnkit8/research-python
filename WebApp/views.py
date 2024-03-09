from django.shortcuts import render
from django.http import HttpResponse

def dashboard_view(request):
    print('yes function is working')
    print('ankit')
    return render(request,'dashboard.html')

def research_paper(request):
    return render(request,'research.html')


def journal_paper(request):
    return render(request,'journal-paper.html')

