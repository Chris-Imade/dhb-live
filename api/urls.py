from django.urls import path
from .views import deposit_api_view, send_newsletter


urlpatterns = [
    path('deposit/', deposit_api_view, name="deposite_api"),
    path('send-newsletter/', send_newsletter, name="send_newsletter"),
    
]