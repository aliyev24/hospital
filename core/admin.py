from django.contrib import admin
from .models import *


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'doctor', 'status')
    list_display_links = ('doctor', 'id')
    list_filter = ('doctor', 'meet_date')


admin.site.register(Department)
admin.site.register(Services)
admin.site.register(Patient)
admin.site.register(Contacts)
admin.site.register(Doctor)
admin.site.register(Treatment)
admin.site.register(Appointment, AppointmentAdmin)
