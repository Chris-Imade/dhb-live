from django.contrib import admin
from .models import Withdrawal, AdminWalletAccount, Account, Transaction, Transfer, Newsletter, ContactUs

# Register your models here.

admin.site.register(Withdrawal)
admin.site.register(AdminWalletAccount)
admin.site.register(Transaction)
admin.site.register(Transfer)
admin.site.register(Account)
admin.site.register(Newsletter)
admin.site.register(ContactUs)

