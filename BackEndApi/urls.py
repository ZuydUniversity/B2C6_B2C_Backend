from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonViewSet

# Create a router and register the PersonViewSet with a URL path
router = DefaultRouter()
router.register(r'person', PersonViewSet)  # Define URL patterns for the PersonViewSet

# URL patterns for the app
urlpatterns = [
    path('', include(router.urls)),  # Include URLs from the router
]