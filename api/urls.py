from django.urls import path
from .views import deposit_api_view


urlpatterns = [
    path('deposit/', deposit_api_view, name="deposite_api")
]