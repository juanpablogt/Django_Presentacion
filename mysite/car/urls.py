from . import views
from django.urls import path

app_name = 'car'

urlpatterns = [
    path('rental_review/', views.rental_review, name='rental_review'),
    path('thank_you/', views.thank_you, name='thank_you'),
]