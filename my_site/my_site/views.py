from django.shortcuts import render
from django.http.response import HttpResponse


articles = {
    "home": "I'm Juan Pablo GT ",
    "contact": "Contact Page",
    "about": "About Page",
    "social": "Social Page",
    "projects": "Projects Page",

}
def home_view(request):
    try:
        return HttpResponse(articles["home"])
    except KeyError:
        return HttpResponse("Key not found")

def contact_view(request):
    try:
        return HttpResponse(articles["contact"])
    except KeyError:
        return HttpResponse("Key not found")
def about_view(request):
    try:
        return HttpResponse(articles["about"])
    except KeyError:
        return HttpResponse("Key not found")
def social_view(request):
    try:
        return HttpResponse(articles["social"])
    except KeyError:
        return HttpResponse("Key not found")
def projects_view(request):
    try:
        return HttpResponse(articles["projects"])
    except KeyError:
        return HttpResponse("Key not found")
