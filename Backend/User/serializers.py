from rest_framework import serializers
from .models import CustomUser, Patient

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'phone_number', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['phone_number', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return Patient.objects.create_user(**validated_data)
