# mybookapp/views.py

from django.shortcuts import render, redirect
from .forms import BookForm,Book

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # Save to DB
            return redirect('book_list')  # After saving, go to list view
    else:
        form = BookForm()
    
    return render(request, 'book_form.html', {'form': form})


def book_list(request):
    books = Book.objects.all()  # Get all books from database
    return render(request, 'book_list.html', {'books': books})