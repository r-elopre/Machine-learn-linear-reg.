from django.urls import path
from .views import hello_world

urlpatterns = [
    path('greet/', hello_world, name='hello_world'),  # Unique route
]
    
