# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='home'),  
    path('stats/', views.book_stats_view, name='book_stats'),
    path('authors/', views.books_by_author_view, name='books_by_author'),
    path('after2020/', views.books_published_after_2020_view, name='books_after_2020'),
]
