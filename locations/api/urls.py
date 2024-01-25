from django.urls import path
from .views import LocationHierarchyAPIView

urlpatterns = [
    path('localities/', LocationHierarchyAPIView.as_view(), name='locality-list'),
    # Add more URL patterns as needed
]
