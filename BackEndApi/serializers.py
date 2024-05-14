from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person # The model we want to use
        fields = '__all__' # The variables we want to store