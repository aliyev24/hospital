from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'docs', views.Doctors, basename='docs')

urlpatterns = [

    path('home/', views.HomePage.as_view(), name='home'),

    path('departments/',
         views.DepartmentList.as_view({'get': 'list'}),
         name='department_list'
         ),
    path('departments/<int:pk>/',
         views.DepartmentList.as_view({'get': 'retrieve'}),
         name='department_detail'
         ),
    path('patients/',
         views.PatientViewSet.as_view({'get': 'list'}),
         name='patient_list'
         ),
    path('patients/<int:pk>',
         views.PatientViewSet.as_view({'get': 'retrieve'}),
         name='patient_detail'
         ),
    path('appointmentlist/',
         views.AppointmentList.as_view({"get": 'list'}),
         name='aplist'
         ),
    path('appointmentlist/<int:pk>/',
         views.AppointmentList.as_view({"get": 'retrieve'}),
         name='aplist_detail'
         ),
    path('doctors/',
         views.Doctors.as_view({'get': 'list'}),
         name='doctor_list'
         ),
]

urlpatterns += router.urls
