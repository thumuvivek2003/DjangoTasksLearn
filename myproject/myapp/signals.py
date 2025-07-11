# myapp/signals.py

from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Book

@receiver(post_save, sender=Book)
def after_book_saved(sender, instance, created, **kwargs):
    if created:
        print(f"📘 New Book Created: {instance.title}")
    else:
        print(f"✏️ Book Updated: {instance.title}")

@receiver(pre_delete, sender=Book)
def before_book_deleted(sender, instance, **kwargs):
    print(f"🗑️ Book is being deleted: {instance.title}")
