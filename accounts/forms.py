from django.forms import ModelForm
from django.contrib.auth.models import User

# Forms
class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
