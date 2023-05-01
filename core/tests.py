from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from accounts.models import CustomUser
from django.utils import timezone

from . import models

now = timezone.now()
User = get_user_model()


class AppointmentTestCase(APITestCase):

    def authenticate(self):
        # Creating users
        self.client.post(
            reverse("signup"),
            {
                "password": "password1235",
                "username": "avaz",
            },
        )
        self.client.post(
            reverse("signup"),
            {
                "password": "password1235",
                "username": "avazinho",
            },
        )
        # Login user
        response = self.client.post(
            reverse("login"),
            {
                "password": "password1235",
                "username": "avaz",
            }
        )
        token = response.data["tokens"]["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    def setUp(self):
        self.authenticate()
        self.user = CustomUser.objects.all()[1:].get()
        self.user2 = CustomUser.objects.all()[:1].get()
        self.department = models.Department.objects.create(title="Cardiology")
        self.patient = models.Patient.objects.create(
            name="Khaleed",
            last_name='Waleed',
            passport=5588,
            time_entry='2022-07-31T08:05:27.205132Z',
            update='2022-09-31T08:05:27.205132Z',
            phone=8887797
        )
        self.ap1 = models.Appointment.objects.create(
            patient=self.patient,
            department=self.department,
            doctor=self.user,
            status="Assigned",
            meet_date=now,
        )
        self.ap2 = models.Appointment.objects.create(
            patient=self.patient,
            department=self.department,
            doctor=self.user2,
            status="Assigned",
            meet_date=now,
        )

    def test_appointment_list(self):
        response = self.client.get(reverse('aplist'))
        result = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result[0]['department'], 'Cardiology')
        self.assertEqual(result[0]['doctor'], 'avaz')

    def test_appointment_detail(self):
        response = self.client.get(
            reverse(
                'aplist_detail',
                kwargs={'pk': self.ap2.id}
            )
        )
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result['Appointment']['status'], 'Assigned')


class DepartmentTestCase(APITestCase):

    def setUp(self):
        self.department = models.Department.objects.create(title="Stomotology")
        models.Services.objects.create(
            title="Dental Bonding",
            department=self.department
        )
        self.department1 = models.Department.objects.create(
            title="Traumatology"
        )

    def test_product_list(self):
        response = self.client.get(reverse('department_list'))
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result[0]["title"], "Stomotology")

    def test_product_detail(self):
        response = self.client.get(
            reverse(
                'department_detail',
                kwargs={'pk': self.department.id}
            )
        )
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result['Department']["title"], "Stomotology")
        self.assertEqual(result['Services'][0]["title"], "Dental Bonding")


class HomeTestCase(APITestCase):

    def setUp(self):
        models.Contacts.objects.create(
            title='Telegram',
            phone=77899,
            email='avaz@mail.ru',
            telegram=777889,
            whatsapp=777899
        )
        self.cat = models.Department.objects.create(title="Stomotology")

    def test_home(self):
        response = self.client.get(reverse('home'))
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result['contacts'][0]["title"], "Telegram")


class PatientTestCase(APITestCase):

    def setUp(self):
        self.client.post(
            reverse("signup"),
            {
                "password": "karvan2004",
                "username": "avaz",
            },
        )
        self.department = models.Department.objects.create(title="Sports")
        self.service = models.Services.objects.create(
            title="Football",
            department=self.department
        )
        self.service2 = models.Services.objects.create(
            title="Dental bonding",
            department=self.department
        )
        self.pat1 = models.Patient.objects.create(
            name="Khaleed", last_name='Waleed',
            passport=5588,
            time_entry='2022-07-31T08:05:27.205132Z',
            update='2022-09-31T08:05:27.205132Z',
            phone=8887797
        )
        self.pat2 = models.Patient.objects.create(
            name="Bunyamin", last_name='Yusuf',
            passport=123447,
            time_entry='2023-03-30T08:05:27.205132Z',
            update='2023-03-31T08:05:27.205132Z',
            phone=98457
        )
        self.user2 = CustomUser.objects.all()[:1].get()
        self.ap2 = models.Appointment.objects.create(
            patient=self.pat2,
            department=self.department,
            doctor=self.user2,
            status="Assigned",
        )

    def test_patient_list(self):
        response = self.client.get(reverse('patient_list'))
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result[1]['name'], "Bunyamin")

    def test_patient_detail(self):
        response = self.client.get(reverse(
            'patient_detail',
            kwargs={'pk': self.pat2.id})
        )
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result['Patient']['passport'], 123447)


class DoctorsTestCase(APITestCase):

    def setUp(self):
        models.Doctor.objects.create(
            name='Matthew',
            surname='Orban',
            biography='London Medical School'
        )
        models.Doctor.objects.create(
            name='Pawel',
            surname='Max',
            biography='Berlin Medical School'
        )

    def test_doctor_list(self):
        response = self.client.get(reverse('doctor_list'))
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result[1]['name'], 'Pawel')
