from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import User
from core.models import Transaction
from django.contrib import messages

# Create your views here
@api_view(['GET', 'POST'])
def deposit_api_view(request):
    if request.method == 'POST':
        user = User.objects.get(id=int(request.data.get('user_id')))
        transaction = Transaction(
            user=user,
            transaction_type=request.data.get("transaction_type"),
            amount=int(request.data.get("amount")),
            selected_asset=request.data.get("transaction_kind"),
        )
        transaction.save()
        messages.success(request, "Your transaction is being processed. A confirmation mail will be sent to you upon confirmation.")
    return Response({})