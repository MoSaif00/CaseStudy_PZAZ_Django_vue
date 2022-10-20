from django.db import models
from django.conf import settings

class Book(models.Model):
    created_at= models.DateTimeField(auto_now_add=True)
    title= models.CharField(max_length=200)
    slug= models.SlugField(max_length=200, unique=True)
    description= models.TextField()
    poster_image= models.ImageField(upload_to='books')
    author= models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE,
                            related_name="books")

    def __str__(self):
        return self.title