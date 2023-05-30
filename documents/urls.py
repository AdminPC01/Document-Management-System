from django.urls import path
from . import views

urlpatterns = [
    path('', views.documents, name='documents'),
    path('single-document/<str:pk>/', views.document, name='documents'),
    path('add-document/', views.add_document, name='add-documents'),
    path('change-document/<str:pk>/', views.change_document, name='change-document'),
]