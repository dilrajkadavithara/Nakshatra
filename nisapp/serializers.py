from rest_framework import serializers
from .models import District, LocalArea, Lead

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['district_id', 'district_name']

class LocalAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalArea
        fields = ['local_area_id', 'local_area_name']

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ['name', 'phone_number', 'district', 'local_area']