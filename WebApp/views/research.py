from django.shortcuts import render
from django.http import HttpResponse


def research_main_view(request):
    return render(request , 'research.html')