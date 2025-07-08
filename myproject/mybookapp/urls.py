# mybookapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.book_create, name='book_create'),
    path('book_list/',views.book_list,name='book_list')
]
