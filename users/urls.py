from django.urls import path

from users.apps import UsersConfig
from users.views import SignupView, SigninView

app_name = UsersConfig.name




urlpatterns = [
    path('', SigninView.as_view(), name='login'),
    path('register/', SignupView.as_view(), name='register'),
]