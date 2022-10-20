from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    url('rest-auth/', include('rest_auth.urls')),
]
