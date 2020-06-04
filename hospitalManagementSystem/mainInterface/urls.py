from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('accounts/login',views.login,name='login'),
    path('accounts/register',views.register,name='register'),
    path('base',views.base,name='base'),
    path('accounts/logout',views.logout,name='logout'),
    path('patient',views.patient,name='patient'),
    path('hr',views.hr,name='hr'),
    path('receptionist',views.receptionist,name='receptionist'),
    path('doctor',views.doctor,name='doctor'),
    path('patient/appointments',views.appointments,name='appointments'),
    path('patient/medicalhistory',views.medicalhistory,name='medicalhistory'),
    path('patient/invoices',views.invoices,name='invoices'),
    path('doctor/appointments',views.appointments_doctor,name='appointments'),
    path('doctor/prescriptions',views.prescription,name='prescription'),
    path('receptionist/dashboard',views.dashboard_receptionist,name='dashboard_receptionist'),
    path('receptionist/createappointment',views.create_appointment,name='create_appointment'),
]
