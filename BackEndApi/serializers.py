from rest_framework import serializers
from .models import Person

# Serializer for the Person model
class PersonSerializer(serializers.ModelSerializer):
    """
    Serializer for the Person model.
    
    A serializer's primary job is to convert data types like the models
    into JSON, XML or other content types so it can be send over the network.
    """
    class Meta:
        model = Person  # Specify the model that the serializer will work with
        fields = '__all__'  # Serialize all fields of the Person model