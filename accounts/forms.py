from django.forms import ModelForm
from django.contrib.auth.models import User

# App model
from accounts.models import Profile

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


class UserForm(ModelForm):
    """
    User form to update the user information in the settings page
    """
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['user']

class ProfileSettingsForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']
