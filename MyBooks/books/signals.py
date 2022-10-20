from django.db.models.signals import pre_save
from .models import Book
from django.dispatch import receiver
from django.utils.text import slugify

@receiver(pre_save, sender = Book)
def add_slug(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.title)
        instance.slug = slug
