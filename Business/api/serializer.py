from rest_framework import serializers
from Business.models import Business

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = [
            'address',
            'phone_number',
            'email',
            'website',
            'description',
            'industry',
            'founded_in',
            'employee_count',
            'id_number',
            'kra_pin',
            'social_media_links',
            'id_attachment'
        ]
        read_only_fields = [
            'is_verified',
            'is_top_rated',
            'created',
            'updated',
            'owner',
        ]


class BusinessUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        exclude = ["owner","id","id_attachment","business_permit","kra_pin_attachment","ceritificate_of_registration","social_media_links", "founded_in","website"]
        read_only_fields=["is_verified","is_top_rated","created" ,"updated",]        
        read_only_fields = ['owner']


