from django.shortcuts import render, redirect
from . import models
from .models import Card

def list(request):
    all_cards = models.Card.objects.all()
    context = {'all_cards': all_cards}
    return render(request, 'card/list.html', context=context)

def add(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mensaje = request.POST['mensaje']
        
        new_card = Card(name=name, email=email, mensaje=mensaje)
        new_card.save()
        
        return redirect('card:list')
    else:
        return render(request, 'card/add.html')


def delete(request):
    if request.method == 'POST':
        pk=request.POST['pk']
        try:
           models.Card.objects.get(pk=pk).delete()
           return render(request, 'card/delete.html')
        except:
            print("Error")
            return redirect('card:list')
    else:
        return render(request, 'card/delete.html')
    
def acerca(request):
    return render(request, 'card/acerca.html')
    
