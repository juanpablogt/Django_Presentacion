from django.urls import path
from . import views

app_name = 'card'

urlpatterns = [
    path('list/', views.list, name='list'),
    path('add/', views.add, name='add'),
    path('delete/', views.delete, name='delete'),
    path('', views.acerca, name='acerca')
]
