from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, "index.html")


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('webApp:dashboard')
        else:
            return render(request, 'login.html', {'error_message': 'Credenciales incorrectas'})

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('webApp:login')


@login_required
def dashboard_view(request):
    user = request.user
    user_name = user.username
    email = user.email
    registration_date = user.date_joined.strftime('%Y-%m-%d %H:%M:%S')

    # Contexto para pasar datos al template
    contexto = {
        'nombre_de_usuario': user_name,
        'correo': email,
        'fecha_de_alta': registration_date,
    }

    # Renderizar la plantilla con el contexto
    return render(request, 'dashboard.html', contexto)
