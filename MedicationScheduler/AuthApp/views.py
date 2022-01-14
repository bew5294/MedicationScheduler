from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, PasswordChangingForm, UpdateUserForm, UpdateUserProfile
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect("MedicationScheduler:front")
        else:
            context['registration_form'] = form
    else:  # GET request
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'register.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('MedicationScheduler:front')
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                print(user)
                login(request, user)
                return redirect('MedicationScheduler:home')
            else:
                print('User not found')
        else:
            # If there were errors, we render the form with these
            # errors
            return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('Auth:login')


def profile_view(request):
    user_update_form = UpdateUserForm(instance=request.user)
    password_change_form = PasswordChangingForm(request.user)
    update_profile_form = UpdateUserProfile()

    if request.method == 'POST' and 'change_password' in request.POST:
        password_change_form = PasswordChangingForm(request.user, request.POST)
        if password_change_form.is_valid():
            password_change_form.save()
            return redirect('Auth:login')
    elif request.method == 'POST' and 'user_update' in request.POST:
        user_update_form = UpdateUserForm(request.POST, instance=request.user)
        if user_update_form.is_valid():
            user_update_form.save()
    elif request.method == 'POST' and 'update_profile_info' in request.POST:
        update_profile_form = UpdateUserProfile(request.POST, instance=request.user)
        if update_profile_form.is_valid():
            update_profile_form.save()

    return render(request, "profile.html",
                  {'password_change_form': password_change_form, "user_update_form": user_update_form,
                   "update_profile_form": update_profile_form})
