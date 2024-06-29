from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='list'),
    path('delete/<item>/',views.delete,name='delete'),
    
    path('update/<item>',views.update, name='update')
    
    
    
]
