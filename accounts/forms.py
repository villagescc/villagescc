from django.forms import ModelForm
from django.contrib.auth.models import User

# Forms
class RegisterForm(ModelForm):
    """ Signup form """

    def __init__(self, *args, **kwargs):
        # Overriding form to set email is required because User email is optional
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
