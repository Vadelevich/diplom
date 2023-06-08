from django.contrib.auth.forms import UsernameField, UserCreationForm, AuthenticationForm

from users.models import User


class SigninForm(AuthenticationForm):
    pass


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)
        field_classes = {"username": UsernameField}
