from django.urls import path
from delivery import views

app_name= 'delivery'

urlpatterns =[
    path('showmap/',views.show_map,name='showmap'),    
]