from django.shortcuts import render
from .models import Project

def home(request):

    projects = None
    return render(request, 'base/home.html',{'projects':projects})
