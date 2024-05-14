from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonViewSet

router = DefaultRouter()
router.register(r'person', PersonViewSet) # URL to access the person view

# App paths
urlpatterns = [
    path('', include(router.urls)), # includes URL in router
]