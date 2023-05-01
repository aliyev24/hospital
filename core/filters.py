from django_filters import rest_framework as rest_filters, CharFilter
from .models import Patient


class PatientFilter(rest_filters.FilterSet):
    name = CharFilter(lookup_expr='icontains')
    last_name = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Patient
        fields = ['name', 'last_name', ]
