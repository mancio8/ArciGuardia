from django.urls import path
from . import views

urlpatterns = [
    path('match/', views.say_hello, name="match"),
    path('match/savedb/', views.savedb, name="savedb"),
    path('risultati/', views.getResult, name="risultati"),
    
    
]