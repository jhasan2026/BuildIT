from django.urls import path
from .views import deleteProfilePic

urlpatterns = [
    # ... other url patterns
    path('delete-profile-pic/', deleteProfilePic, name='deleteProfilePic'),  # Adjust the URL path as necessary
]
