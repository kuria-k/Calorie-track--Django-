from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),        
    path('add/', views.add_food, name='input'),     
    path('data/', views.view_food, name='data'), 
    path('delete/<int:item_id>/', views.delete_food, name='delete_food'),
   
]

