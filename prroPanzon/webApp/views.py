from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import AppUserCreationForm

# Create your views here.

def index(request):
    return render(request, "index.html")


def login_view(request):
    if request.method != 'POST':
        return render(request, 'login.html', {'form': AuthenticationForm()})

    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('webApp:dashboard')
        else:
            messages.error(request, 'Error al iniciar sesion. Intente mas tarde')

    return render(request, 'login.html', {'error_message': 'Credenciales incorrectas'})


def logout_view(request):
    logout(request)
    return redirect('webApp:index')


@login_required
def dashboard_view(request):
    user = request.user
    user_name = user.username
    email = user.email
    registration_date = user.date_joined.strftime('%Y-%m-%d %H:%M:%S')

    contexto = {
        'nombre_de_usuario': user_name,
        'correo': email,
        'fecha_de_alta': registration_date,
    }

    return render(request, 'dashboard.html', contexto)


def signup_view(request):
    if request.method == 'POST':
        form = AppUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('webApp:dashboard')
    else:
        form = AppUserCreationForm()

    return render(request, 'signup.html', {'form': form})

