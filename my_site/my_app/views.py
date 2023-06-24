from django.shortcuts import render
from django.http import HttpResponse


def home_view(request, topic):
    return render(request, "my_app/Templates/maqueta1.html" , {"topic": topic})