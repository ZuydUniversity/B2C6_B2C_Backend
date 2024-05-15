from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerializer

# ViewSet for CRUD operations on person data
class PersonViewSet(viewsets.ModelViewSet):
    """
    ViewSet for CRUD operations on person data.

    This ViewSet provides endpoints for creating, retrieving,
    updating, and deleting person records.
    """
    queryset = Person.objects.all()  # Queryset of all Person records
    serializer_class = PersonSerializer  # Specify the serializer to use for serialization