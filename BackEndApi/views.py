from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerializer

# The view of the person model
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all() # The dataset we want to query when calling this view
    serializer_class = PersonSerializer # The serializer this view needs to use