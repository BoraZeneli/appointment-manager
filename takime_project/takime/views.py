from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Appointment, Client
from .forms import AppointmentForm, ClientForm
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required  # << this line was missing
from .forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}. You can log in now.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'takime/register.html', {'form': form})

@login_required(login_url='login')
def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']

            # Check if client already exists
            if Client.objects.filter(first_name__iexact=first_name,
                                     last_name__iexact=last_name,
                                     phone_number=phone_number).exists():
                messages.error(request, "This client already exists.")
            else:
                form.save()
                messages.success(request, "Client added successfully.")
                return redirect('appointment_list')
    else:
        form = ClientForm()
    
    return render(request, 'takime/add_client.html', {'form': form})

@login_required(login_url='login')
def appointment_list(request):
    search_query = request.GET.get('search', '')
    appointments = Appointment.objects.all().select_related('client')

    if search_query:
        appointments = appointments.filter(
            Q(client__first_name__icontains=search_query) | 
            Q(client__last_name__icontains=search_query)
        )

    paginator = Paginator(appointments.order_by('date', 'start_time'), 10)  # 10 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'takime/appointment_list.html', {'appointments': page_obj, 'search_query': search_query})

@login_required(login_url='login')
def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            new_appointment = form.save(commit=False)

            # Check for overlapping appointments
            overlapping = Appointment.objects.filter(
                Q(start_time__lt=new_appointment.end_time) & 
                Q(end_time__gt=new_appointment.start_time)
            ).exists()

            if overlapping:
                messages.error(request, "There is already an appointment scheduled for this date and time.")
                return render(request, 'takime/add_appointment.html', {'form': form, 'overlapping': True})

            new_appointment.save()
            messages.success(request, "Appointment added successfully.")
            return redirect('appointment_list')
    else:
        form = AppointmentForm()

    return render(request, 'takime/add_appointment.html', {'form': form})

@login_required(login_url='login')
def edit_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            edited_appointment = form.save(commit=False)

            # Check for overlapping appointments on the same date and time, excluding current one
            overlapping = Appointment.objects.filter(
                date=edited_appointment.date,
                start_time__lt=edited_appointment.end_time,
                end_time__gt=edited_appointment.start_time
            ).exclude(pk=pk).exists()

            if overlapping:
                messages.error(request, "There is already an appointment scheduled for this date and time.")
                return render(request, 'takime/edit_appointment.html', {'form': form})
            
            edited_appointment.save()
            messages.success(request, "Appointment updated successfully.")
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    
    return render(request, 'takime/edit_appointment.html', {'form': form})


@login_required(login_url='login')
def delete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        messages.success(request, "Appointment deleted successfully.")
        return redirect('appointment_list')
    return render(request, 'takime/confirm_delete.html', {'appointment': appointment})


# Function to send reminders for appointments scheduled for tomorrow
def send_reminder_notifications():
    upcoming = Appointment.objects.filter(
        date=timezone.localdate() + timedelta(days=1)
    )
    for appointment in upcoming:
        # Here you would integrate an SMS/email API if you use one
        print(f"Reminder for {appointment.client} on {appointment.date} at {appointment.start_time}")
