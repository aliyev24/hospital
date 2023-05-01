from drf_yasg.utils import swagger_auto_schema
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import GenericViewSet
from datetime import datetime, timedelta, time
from rest_framework import viewsets, filters
from django_filters import rest_framework as rest_filters

from .filters import PatientFilter
from . import serializers
from . import models


class HomePage(ListAPIView):
    serializer_class = serializers.DepartmentSerializer

    def list(self, request):
        contacts = serializers.ContactSerializer(
            models.Contacts.objects.all(), many=True)
        departments = serializers.DepartmentSerializer(
            models.Department.objects.all(),
            many=True
        )
        context = {'contacts': contacts.data, 'departments': departments.data}
        return Response(context)


class DepartmentList(viewsets.ReadOnlyModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer

    @swagger_auto_schema(
        operation_summary='Department detail and services of that department.'
    )
    def retrieve(self, request, *args, **kwargs):
        """
        Department and services of that department provided.
        """
        instance = self.get_object()
        department = self.get_serializer(instance)
        services = models.Services.objects.filter(department_id=instance.id)
        services_serialized = serializers.ServiceSerializer(
            services,
            many=True
        )
        result = {'Department': department.data,
                  'Services': services_serialized.data}
        return Response(result)


class Doctors(viewsets.ReadOnlyModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer


class AppointmentList(viewsets.ModelViewSet):
    """
    List of doctor's appointments scheduled for today.
    """
    serializer_class = serializers.AppointmentSerializer

    def get_queryset(self):
        user = self.request.user
        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())
        return models.Appointment.objects.filter(
            doctor=user,
            meet_date__lte=today_end,  # Appointments for today
            meet_date__gte=today_start,  # Appointments for today
            status='Assigned'
        ).order_by('-meet_date')

    def retrieve(self, request, *args, **kwargs):
        user = self.request.user
        instance = self.get_object()
        appointment = models.Appointment.objects.filter(
            doctor=user
        ).get(id=instance.id)
        appointment_serialized = serializers.AppointmentSerializer(appointment)
        result = {'Appointment': appointment_serialized.data}
        return Response(result)


class PatientViewSet(ListModelMixin, GenericViewSet):
    serializer_class = serializers.PatientSerializer
    queryset = models.Patient.objects.all()
    filter_backends = (rest_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = PatientFilter
    search_fields = ['name', 'last_name']

    def get_appointment(self, pk):
        """
        Getting all appointments patient had.
        """
        appointments = serializers.AppointmentSerializer(
            models.Appointment.objects.all().filter(
                patient_id=pk),
                many=True
        )
        return appointments

    @swagger_auto_schema(
        operation_summary="Patient's data and all appointments. "
    )
    def retrieve(self, request, pk):
        item = self.get_object()
        serializer = self.get_serializer(item)
        appointments = self.get_appointment(pk)
        result = {
            'Appointments': appointments.data,
            'Patient': serializer.data
        }
        return Response(result)
