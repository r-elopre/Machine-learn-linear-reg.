from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('greet/', views.hello_world, name='hello_world'),  # Existing route for greeting
    path('save_data/', views.save_data, name='save_data'),  # Save data route
    path('predict/', views.predict, name='predict'),  # Predict route
]

