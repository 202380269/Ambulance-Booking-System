from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def register_view(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        login(request, user)  # auto login after register
        return redirect('dashboard')

    return render(request, 'bookings/register.html', {'form': form})


def dashboard(request):
    return render(request, 'bookings/dashboard.html')