from django.shortcuts import render
from django.http.response import HttpResponse

articles = {
    "home": " 666 Juan Pablo",
    "contact": "Contact Page",
    "about": "About Page",
    "social": "Social Page",
    "projects": "Projects Page",
    "error": "Error Page"

}

# Create your views here.
def home_view(request):
    return HttpResponse(articles["home"])

def contact_view(request):

    return HttpResponse(articles["contact"])

def about_view(request):

    return HttpResponse(articles["about"])

def social_view(request):

    return HttpResponse(articles["social"])

def projects_view(request):

    return HttpResponse(articles["projects"])

