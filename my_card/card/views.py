from django.shortcuts import render

# Create your views here.

def list(request):
    return render(request, 'card/list.html')

def add(request):
    return render(request, 'card/add.html')

def delete(request):
    return render(request, 'card/delete.html')
