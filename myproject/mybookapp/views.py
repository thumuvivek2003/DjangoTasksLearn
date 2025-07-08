# mybookapp/views.py

from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()  # Get all books from database
    return render(request, 'book_list.html', {'books': books})
