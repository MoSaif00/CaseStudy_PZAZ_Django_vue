from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
# from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
# from django.contrib.auth.models import User
from .permissions import IsAuthor

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('-created_at')
    lookup_field = 'slug'
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAuthor]
    # def get_permissions(self):
    #     if self.action in ['update', 'partial_update', 'destroy','create']:
    #         self.permission_classes = [IsAuthenticated, ]
    #     elif self.action in ['list']:
    #         self.permission_classes = [AllowAny, ]
    #     return super().get_permissions()
    # authentication_classes = (TokenAuthentication,)

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)
