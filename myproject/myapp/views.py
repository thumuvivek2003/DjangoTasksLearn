# myapp/views.py

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book
from django.urls import reverse_lazy

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Book
    template_name = 'book_form.html'
    fields = ['title', 'author', 'published_date']
    success_url = reverse_lazy('book_list')

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book_form.html'
    fields = ['title', 'author', 'published_date']
    success_url = reverse_lazy('book_list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book_list')
