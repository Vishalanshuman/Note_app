from django.urls import path
from .views import SignupView, LoginView, LogoutView

urlpatterns = [
    path("signup/", SignupView.as_view(), name="singup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

    
]

