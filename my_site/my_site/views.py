from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.response import HttpResponse
from django.http.response import HttpResponseNotFound, HttpResponseServerError, Http404, HttpResponseRedirect

articles = {
    "home": "5555 Juan Pablo GT ",
    "contact": "Contact Page",
    "about": "About Page",
    "social": "Social Page",
    "projects": "Projects Page",
}

def home_view(request,topic):
    try:
        result = articles[topic]
        return HttpResponse(result)
    except:
        raise Http404("404 GENERIC ERROR PAGE")
    
def contact_view(request,topic):
    try:
        result = articles[topic]
        return HttpResponse(result)
    except:
        raise Http404("404 GENERIC ERROR PAGE")
    
def about_view(request,topic):
    try:
        result = articles[topic]
        return HttpResponse(result)
    except:
        raise Http404("404 GENERIC ERROR PAGE")
    
def social_view(request,topic):
    try:
        result = articles[topic]
        return HttpResponse(result)
    except:
        raise Http404("404 GENERIC ERROR PAGE")
    
def projects_view(request,topic):
    try:
        result = articles[topic]
        return HttpResponse(result)
    except:
        raise Http404("404 GENERIC ERROR PAGE")
    
