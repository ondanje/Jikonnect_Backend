from rest_framework import serializers

from locations.models import Locality

class LocalitySerializer(serializers.ModelSerializer): 
    class Meta:
        model = Locality
        fields = ['name','id', 'subcounty', 'county', 'is_city']
        depth = 1 