from django.urls import path
from . import views

urlpatterns = [
    path('documents/', views.Documents, name='documents'),
    path('documents/<str:pk>/', views.Document, name='documents'),
    path('add-document/', views.addDocument, name='add-documents'),
    path('change-document/<str::pk>/', views.changeDocument, name='change-documents'),
]