from django.contrib import admin
from .models import Withdrawal, AdminWalletAccount, Transaction

# Register your models here.

admin.site.register(Withdrawal)
admin.site.register(AdminWalletAccount)
admin.site.register(Transaction)

