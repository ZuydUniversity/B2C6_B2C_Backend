from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, DocterCreateView, DocterDeleteView, DocterDetailView

router = DefaultRouter()
router.register(r'docters', DoctorViewSet, basename='doctor')


urlpatterns = [
    path('', include(router.urls)),
    path('doctercreate/', DocterCreateView.as_view(), name='docter-create'),
    path('docter/<int:pk>/', DocterDetailView.as_view(), name='docter-detail'),
    path('docterdelete/<int:pk>/', DocterDeleteView.as_view(), name='docter-delete'),
]