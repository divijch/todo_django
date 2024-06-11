from django.urls import path, include
from . import views

urlpatterns = [
    
    
    path('addtask/', views.addtask, name = 'addtask'),
    path('mark_as_done/<int:pk>', views.mark_as_done, name='mark_as_done'),
    
]