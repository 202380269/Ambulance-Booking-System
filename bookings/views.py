from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Booking
from .forms import BookingForm


def register_view(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        login(request, user)  # auto login after register
        return redirect('dashboard')

    return render(request, 'bookings/register.html', {'form': form})


def dashboard(request):
    bookings = Booking.objects.all().order_by('-created_at')
    return render(request, 'bookings/dashboard.html', {'bookings': bookings})


def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BookingForm()

    return render(request, 'bookings/create_booking.html', {'form': form})