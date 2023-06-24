from django.urls import path
from . import views


urlpatterns = [
    path('<topics>/', views.home_view, name='home'),

]
