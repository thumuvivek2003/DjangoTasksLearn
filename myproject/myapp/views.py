# myapp/views.py

from django.db.models import Count, Max, Min, Avg
from django.shortcuts import render
from .models import Book


def index_view(request):
    return render(request, 'index.html')


def book_stats_view(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        earliest=Min('published_date'),
        latest=Max('published_date'),
    )
    return render(request, 'book_stats.html', {'stats': stats})


def books_by_author_view(request):
    data = Book.objects.values('author').annotate(book_count=Count('id')).order_by('-book_count')
    return render(request, 'books_by_author.html', {'data': data})


from django.db import connection

def books_published_after_2020_view(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, title, author, published_date FROM myapp_book WHERE published_date >= '2020-01-01'")
        rows = cursor.fetchall()

    books = [
        {'id': row[0], 'title': row[1], 'author': row[2], 'published_date': row[3]}
        for row in rows
    ]

    return render(request, 'books_after_2020.html', {'books': books})


