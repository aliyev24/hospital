from rest_framework import serializers
from . import models
from accounts.models import CustomUser


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Services
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    doctor = serializers.SlugRelatedField(
        slug_field="username",
        queryset=CustomUser.objects.all()
    )
    patient = serializers.SlugRelatedField(
        slug_field="name",
        queryset=models.Patient.objects.all()
    )
    department = serializers.SlugRelatedField(
        slug_field="title",
        queryset=models.Department.objects.all()
    )

    class Meta:
        model = models.Appointment
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Doctor
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contacts
        fields = '__all__'


class TreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Treatment
        fields = '__all__'
