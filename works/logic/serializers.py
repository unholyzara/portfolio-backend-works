from rest_framework import serializers

from .models import Company, Work


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["active", "name", "phone_number", "email", "slug"]


class WorkSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Work
        fields = ["active", "date_from", "date_to", "company", "role", "slug"]
