# mybookapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('api/books/', views.book_list_create, name='book_list_create'),
    path('api/books/<int:pk>/', views.book_detail, name='book_detail'),
]
