from django.shortcuts import render,redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
from .models import Appointments,MedicalHistory,Invoices,Doctor,Patient
# Create your views here.
def base(request):
    return render(request,'base.html')
def home(request):
    return render(request,'index.html')
def register(request):
    print('hello hello'+request.method)
    if request.method=='POST':

        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        print(first_name)
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        register_as=request.POST['registeras']
        # 0 = patient  1= doctor
        

        print('hello hello')
        print(register_as)
        print(type(register_as))
        is_staff=False
        if register_as=='1':
            is_staff=True
        print(is_staff)
        #super_user=doctor patient=nothing
        if password1==password2:
            if User.objects.filter(username= username).exists():
                messages.info(request,'Username taken')
                print('Username taken')
                return redirect('register')
            elif User.objects.filter(email= email).exists():
                messages.info(request,'Email taken')
                print('Email taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name,is_superuser=is_staff)
                user.save()
                if(is_staff):
                    doctor=Doctor()
                    doctor.firstname=first_name
                    doctor.lastname=last_name
                    doctor.specialization="Physician"
                    doctor.salary=100000
                    doctor.save()
                else:
                    patient=Patient()
                    patient.firstname=first_name
                    patient.lastname=last_name
                    patient.save()

                print('User Created')
                return redirect('login')
        else: 
            print(request,'Password not matching')
            messages.info(request,'Password not matching')
            return redirect('register')
      
    else:
      
        return render(request,'register.html')

def login(request):

     if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username= username, password= password)
        print(type(user))
        if user is not None:
            auth.login(request,user)
            if(user.is_staff==False and user.is_superuser==False):
                return redirect("/patient")
            elif(user.is_staff==True and user.is_superuser==False):
                 return redirect("/receptionist")
            elif(user.is_staff==False and user.is_superuser==True):
                 return redirect("/doctor")
            elif(user.is_staff==True and user.is_superuser==True):
                return redirect("/hr")
        else:
            print(request,"invalid Credentials")
            messages.info(request,"invalid Credentials")
            return redirect("login")
     else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect("/")
def patient(request):
    return render(request,'patient_dashboard.html')

def hr(request):
    return render(request,'hr_dashboard.html')

def doctor(request):
    return render(request,'doctor_dashboard.html')

def receptionist(request):
    return render(request,'receptionist_dashboard.html')

def appointments(request):
    appoints=Appointments.objects.filter(username=request.user.username)
    return render(request,'appointments.html',{'appoints':appoints})
def medicalhistory(request):
    hists=MedicalHistory.objects.filter(username=request.user.username)
    return render(request,'medicalhistory.html',{'hists':hists})

def invoices(request):
    invoices=Invoices.objects.filter(username=request.user.username)
    return render(request,'invoices.html',{'invoices':invoices})
def appointments_doctor(request):
    appoints=Appointments.objects.filter(doctor=request.user.username)
    return render(request,'appointments_doctor.html',{'appoints':appoints})
def prescription(request):
    hists=MedicalHistory.objects.all()
    return render(request,'prescription.html',{'hists':hists})

def dashboard_receptionist(request):
    appoints=Appointments.objects.all()
    pending=Appointments.objects.filter(status='Pending').count()
    completed=Appointments.objects.filter(status='Completed').count()
    return render(request,'dash_receptionist.html',{'appoints':appoints,'pending':pending,'completed':completed})

def create_appointment(request):
    if(request.method=='POST'):
        date=request.POST['date']
        time=request.POST['time']
        username=request.POST['username']
        doctor=request.POST['doctor']
        status=request.POST['status']
        appoint=Appointments()
        appoint.doctor=doctor
        appoint.date=date
        appoint.status=status
        appoint.username=username
        appoint.time=time
        appoint.save()
        return redirect('dashboard_receptionist')
    else:
        return render(request,'create_appointment.html')