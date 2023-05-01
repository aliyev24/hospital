from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import get_user_model

USER = get_user_model()


class Patient(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    balance = models.IntegerField(default=0, null=True, blank=True)
    payment_made = models.BooleanField(default=False)
    passport = models.PositiveIntegerField()
    time_entry = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(auto_now=True)
    phone = models.IntegerField()

    def __str__(self):
        return self.name + " " + self.last_name


class Department(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    department = models.ForeignKey(
        Department,
        related_name='Services',
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['title']


class Treatment(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    made_at = models.DateTimeField(auto_now_add=True, verbose_name="Made at")
    description = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.title


class Appointment(models.Model):
    Status_CHOICES = (
        ("Visited", "Visited"),
        ("Assigned", "Assigned"),
        ("Cancelled", "Cancelled"),
        ("Reassigned", "Reassigned"),
    )
    Priority_CHOICES = (
        ("Important", "Important"),
        ("Routine", "Routine"),
    )
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(USER,
                               on_delete=models.PROTECT,
                               related_name="doctor",
                               verbose_name="Doctor")
    treatment = models.ForeignKey(
        Treatment,
        related_name='treatments',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    meet_date = models.DateTimeField(default=now)
    description = models.TextField(null=True)
    comment = models.TextField(null=True, blank=True)
    priority = models.CharField(
        max_length=50,
        verbose_name="Priority",
        choices=Priority_CHOICES,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=50,
        verbose_name="Status",
        choices=Status_CHOICES,
        null=True,
        blank=True
    )
    department = models.ForeignKey(
        Department,
        null=True,
        on_delete=models.SET_NULL
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'need ' + str(self.department) + ' at ' + str(self.meet_date)

    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'
        ordering = ['-created_at']


class Contacts(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    telegram = models.CharField(max_length=255, null=True, blank=True)
    whatsapp = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


class Doctor(models.Model):
    CHOICES = (
        ("Not chosen", "Not chosen"),
        ("Stomatology", "Stomatology"),
        ("Diagnostic Ultrasound", "Diagnostic Ultrasound"),
        ("Psychological Consultation", "Psychological Consultation"),
        ("Traumatology", "Traumatology"),
    )
    name = models.CharField(max_length=255, null=True, blank=True)
    surname = models.CharField(max_length=255, null=True, blank=True)
    biography = models.TextField(max_length=2500, null=True, blank=True)
    department = models.CharField(
        max_length=50,
        verbose_name="Department",
        choices=CHOICES,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name + ' ' + self.surname

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'
