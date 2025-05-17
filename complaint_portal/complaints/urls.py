#This file defines URL patterns that map URLs to specific views in your complaints app.


from django.urls import path#Used to define URL patterns.
from . import views#Connects URLs to view functions.

urlpatterns = [
    path('', views.dashboard, name='dashboard'),#Maps homepage (/) to the dashboard view.
    path('add/', views.add_complaint, name='add_complaint'),#Allows users to submit a new complaint.
    path('view/<int:pk>/', views.view_complaint, name='view_complaint'),
    # path('complaint/<int:pk>/edit/', views.edit_complaint, name='edit_complaint'),
    # path('update-status/<int:complaint_id>/', views.update_status, name='update_status'),
    path('complaint/<int:complaint_id>/edit/', views.edit_complaint, name='edit_complaint'),
   # Add this to your urlpatterns list in urls.py
path('update-status/<int:complaint_id>/', views.update_status, name='update_status'),
]