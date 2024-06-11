from django.urls import path, include
from . import views

urlpatterns = [
    
    #Add Task Feature
    path('addtask/', views.addtask, name = 'addtask'),
    
    #Mark As Done Feature
    path('mark_as_done/<int:pk>', views.mark_as_done, name='mark_as_done'),
    
    #Mark As Undone Feature
    path('mark_as_undone/<int:pk>', views.mark_as_undone, name  = 'mark_as_undone'),
    
    #Edit Feature
    path('edit_task/<int:pk>', views.edit_task, name = 'edit_task'),
    
    #Delete Feature
    path('delete_task/<int:pk>', views.delete_task, name = 'delete_task'),
    
    
]