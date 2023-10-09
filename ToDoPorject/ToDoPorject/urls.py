# urls.py in your project directory
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),  # Includes the URL patterns from tasks/urls.py
]
