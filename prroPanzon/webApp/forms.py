from django.contrib.auth.forms import UserCreationForm
from .models import AppUser

class AppUserCreationForm(UserCreationForm):

    class Meta:
        model = AppUser
        fields = fields = ('username', 'email', 'password1', 'password2')

