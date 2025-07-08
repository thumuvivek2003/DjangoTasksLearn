from django.contrib import admin
from .models import Book,BookAdmin

# admin.site.register(Book)
admin.site.register(Book, BookAdmin)
