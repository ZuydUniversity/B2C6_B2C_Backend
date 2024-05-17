from rest_framework import viewsets
from .models import Docter
from .serializer import DocterSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Docter.objects.all()
    serializer_class = DocterSerializer

class DocterCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = DocterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DocterDeleteView(DestroyAPIView):
    queryset = Docter.objects.all()
    serializer_class = DocterSerializer

class DocterDetailView(RetrieveAPIView):
    queryset = Docter.objects.all()
    serializer_class = DocterSerializer