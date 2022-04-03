from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"course/index.html")

def about(request):
    return render(request, "course/about.html")

def contact(request):
    return render(request, "course/contact.html")

def services(request):
    return render(request, "course/services.html")

def courses(request):
    return render(request, "course/courses.html")