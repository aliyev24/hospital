from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from . import models


@receiver(post_save, sender=models.Patient)
def make_balance(sender, instance, created, **kwargs):
    """
    When Patient created balance set to 0.
    """
    if created:
        instance.balance = 0
        instance.save()


@receiver(post_save, sender=models.Appointment)
def valid_order(sender, instance, created, **kwargs):
    """
    When Appointment created adds 30 to patient's balance
    if there is Treatment or not.
    """
    if created:
        patient = models.Patient.objects.get(id=instance.patient.id)
        if instance.treatment is None:
            patient.balance += 30
            patient.save()


@receiver(pre_save, sender=models.Appointment)
def valid_order(sender, instance, **kwargs):
    """
    When Treatment added to appointment
    then treatment price being added to balance of patient.
    """
    patient = models.Patient.objects.get(id=instance.patient.id)
    if instance.treatment is not None:
        price = instance.treatment.price
        patient.balance += price
        patient.save()


@receiver(post_save, sender=models.Patient)
def payment_confirmed(sender, instance, **kwargs):
    """
    When user pays nulls Patient's balance.
    """
    if instance.payment_made is True:
        instance.balance = 0
        instance.payment_made = False
        instance.save()
