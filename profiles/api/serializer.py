from rest_framework import serializers
from profiles.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['user','id','id_field']
        read_only_fields = ['user']



class ProfileSerializer(serializers.ModelSerializer):
    phone_number = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        exclude = ['user', 'id', 'id_field']
        read_only_fields = ['user']

    def get_phone_number(self, instance):
        return instance.phone_number

