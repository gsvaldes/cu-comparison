from rest_framework import serializers

from locator.models import Business


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ('id', 'business_name', 'link', 'business_type')
