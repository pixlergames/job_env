from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('job-listing', views.job_listing, name='job-listing'),
    path('job-details/<int:pk>/', views.job_details, name='job-details'),
    path('compete-listing', views.compete_listing, name='compete-listing'),
    path('compete-details/<int:pk>/', views.compete_details, name='compete-details'),
]
