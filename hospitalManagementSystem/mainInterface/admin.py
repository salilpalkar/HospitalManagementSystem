from django.contrib import admin
from .models import User,Appointments,MedicalHistory,Invoices,Doctor,Patient
# Register your models here.
admin.site.register(User)
admin.site.register(Appointments)
admin.site.register(MedicalHistory)
admin.site.register(Invoices)
admin.site.register(Doctor)
admin.site.register(Patient)