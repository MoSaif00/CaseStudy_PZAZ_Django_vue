from django.contrib import admin
from .models import Book    

admin.site.register(Book)

# from django.contrib import admin
# from .models import Book
# # Register your models here.

# # admin.site.register(Book)

# @admin.register(Book)
# class BookModel(admin.ModelAdmin):
#     list_filter= ('title', 'description')
#     list_display= ('title', 'description')