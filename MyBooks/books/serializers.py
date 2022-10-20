from rest_framework import serializers
from .models import Book
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token


class BookSerializer(serializers.ModelSerializer):
    # Allow Url for image field
    poster_image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    slug = serializers.SlugField(read_only=True)
    author = serializers.StringRelatedField()

    class Meta: 
        model = Book
        fields = "__all__"


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'password']

#         # Hide password
#         extra_kwargs = {'password':{
#             'write_only':True,
#             'required':True,
#         }}
    
#     # Hash password when creating new user
#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         # add token to user
#         Token.objects.create(user=user)
#         return user