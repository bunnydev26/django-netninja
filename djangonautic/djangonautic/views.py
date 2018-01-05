from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("This is the homepage")
    return render(request, "homepage.html")

def about(request):
    #return HttpResponse("This is about page")
    return render(request, "about.html")
