from django.shortcuts import render, HttpResponse, redirect

from django.core.files.storage import FileSystemStorage

# Create your views here.
def homepage(request):
    return render(request, "homepage.html")

def index(request):
    return render(request, "adminpanel.html")

def sign_in(request):
    return render(request, "signin.html")

def sign_up(request):
    return render(request, "signup.html")

def testimonial(request):
    return render(request, "about.html")



