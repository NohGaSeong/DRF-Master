"""
master url
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/auth/', include("authentication.urls")),
    path('api/todos/', include("todos.urls")),
    path('admin/', admin.site.urls),
    
]
