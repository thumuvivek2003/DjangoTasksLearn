# mybookapp/urls.py

from django.urls import path
from .views import BookListAPIView

urlpatterns = [
    path('api/books/', BookListAPIView.as_view(), name='api_books'),
]
