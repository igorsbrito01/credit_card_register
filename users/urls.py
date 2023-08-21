from django.urls import path

from .views import LoginView, logoutView

urlpatterns = [path("login", LoginView.as_view()), path("logout", logoutView.as_view())]
