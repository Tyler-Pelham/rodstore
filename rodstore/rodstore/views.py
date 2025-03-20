from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello Everybody!")
    return render(request, "home.html")


def about(request):
    #return HttpResponse("About My Site")
    return render(request, "about.html")

