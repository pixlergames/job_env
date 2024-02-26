from django.urls import path
from . import views

urlpatterns = [
    
    path('create-compete/', views.create_compete, name='create-compete'),
    path('update-compete/<int:pk>/', views.update_compete, name='update-compete'),
    path('delete-compete/<int:pk>/', views.delete_compete, name='delete-compete'),
    path('manage-compete/', views.manage_compete, name ='manage-compete'),
    path('apply-to-compete/<int:pk>',views.apply_to_compete, name ='apply-to-compete'),
    path('all-applicants/<int:pk>/', views.all_applicants, name = 'all-applicants'),
    path('applied-compete',views.applied_compete, name ='applied-compete')
    
    
]
