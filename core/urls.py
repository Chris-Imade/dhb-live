from django.urls import path
from .views import (
    home,
    contact,
    about,
    dashboard,
    settings,
    deposit,
    history,
    withdraw,
    transfer
)

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('dashboard/', dashboard, name="dashboard"),
    path('settings/', settings, name="settings"),
    path('deposit/', deposit, name="deposit"),
    path('history/', history, name="history"),
    path('withdraw/', withdraw, name="withdraw"),
    path('transfer/', transfer, name="transfer"),
]
