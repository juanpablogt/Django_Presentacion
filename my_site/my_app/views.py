from django.shortcuts import render
from django.http import HttpResponse

def simple_view(request):
    return render(request,'first_app/maqueta.html')

def contact_view(request):
    
    my_var = {'first_name':'pablo','last_name':'gonzalez', 'age':'32'}
    return render(request,'first_app/contact.html',context= my_var)

