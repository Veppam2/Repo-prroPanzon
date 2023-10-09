from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def index(request):
    return render(request, "index.html")


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('webApp:dashboard')
        else:
            return render(request, 'login.html', {'error_message': 'Credenciales incorrectas'})
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


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
