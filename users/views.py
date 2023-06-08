from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.form import SignupForm, SigninForm
from users.models import User


class SigninView(LoginView):
    template_name = 'users/login.html'
    form_class = SigninForm

class SignupView(CreateView):
    template_name = 'users/register.html'
    model = User
    form_class = SignupForm
    success_url = reverse_lazy('diagnostic:home')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
        return super().form_valid(form)
