from django.db import models
from accounts.models import User
from django.db.models.signals import post_save
from .utils import random_string
# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="User")
    account_number = models.IntegerField(verbose_name="Account Number", blank=True, null=True)
    account_name = models.CharField(verbose_name="Account Name", max_length=100, blank=True, null=True)
    bank_name = models.CharField(verbose_name="Bank Name", max_length=100, blank=True, null=True)
    bitcoin_address = models.CharField(verbose_name="Bitcoin Address", max_length=200, blank=True)
    etherium_address = models.CharField(verbose_name="Etherium Address", max_length=200, blank=True)
    cashtag = models.CharField(verbose_name="CashTag", max_length=200, blank=True, null=True)
    swift_code = models.CharField(verbose_name="Swift Code", max_length=200, blank=True, null=True)
    paypal_email = models.CharField(verbose_name="Paypal Email", max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
    
    

def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Account.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
	instance.account.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)

class Withdrawal(models.Model):
    ASSET_SELECTED = [
        ("Bitcoin", "Bitcoin"),
        ("Etherium", "Etherium"),
        ("BankTransfer", "BankTransfer"),
        ("Paypal", "Paypal"),
        ("CashApp", "CashApp")
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    balance_type = models.CharField(verbose_name="Balance Type", max_length=200, blank=True, null=True)
    selected_asset = models.CharField(verbose_name="Transaction Type", max_length=200, choices=ASSET_SELECTED, blank=False, null=False)
    
    # Ethereum Withdrawal
    ethereum_address = models.CharField(verbose_name="Ethereum Address", max_length=200, blank=True, null=True)
    
    # Bitcoin Withdrawal
    bitcoin_address = models.CharField(verbose_name="Bitcoin Address", max_length=200, blank=True, null=True)
    
    # Account Details
    account_name = models.CharField(verbose_name="Account Name", max_length=200, blank=True, null=True)
    account_number = models.CharField(verbose_name="Account Number", max_length=200, blank=True, null=True)
    bank_name = models.CharField(verbose_name="Bank Name", max_length=200, blank=True, null=True)
    swift_code = models.CharField(verbose_name="Swift Code", max_length=200, blank=True, null=True)
    paypal_email = models.CharField(verbose_name="Paypal Email", max_length=200, blank=True, null=True)
    cashtag = models.CharField(verbose_name="Cash Tag", max_length=200, blank=True, null=True)
    
    amount = models.IntegerField(verbose_name="Amount", blank=False, null=False)


class Transfer(models.Model):
    ASSET_SELECTED = [
        ("Bitcoin", "Bitcoin"),
        ("Etherium", "Etherium"),
        ("BankTransfer", "BankTransfer"),
        ("Paypal", "Paypal"),
        ("CashApp", "CashApp")
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    custom_id = models.CharField(max_length=500, blank=True, null=True, default=random_string)
    balance_type = models.CharField(verbose_name="Balance Type", max_length=200, blank=True, null=True)
    selected_asset = models.CharField(verbose_name="Transaction Type", max_length=200, choices=ASSET_SELECTED, blank=False, null=False)
    
    # Ethereum Transfer
    ethereum_address = models.CharField(verbose_name="Ethereum Address", max_length=200, blank=True, null=True)
    
    # Bitcoin Transfer
    bitcoin_address = models.CharField(verbose_name="Bitcoin Address", max_length=200, blank=True, null=True)
    
    # Account Details
    account_name = models.CharField(verbose_name="Account Name", max_length=200, blank=True, null=True)
    account_number = models.CharField(verbose_name="Account Number", max_length=200, blank=True, null=True)
    bank_name = models.CharField(verbose_name="Bank Name", max_length=200, blank=True, null=True)
    swift_code = models.CharField(verbose_name="Swift Code", max_length=200, blank=True, null=True)
    paypal_email = models.CharField(verbose_name="Paypal Email", max_length=200, blank=True, null=True)
    cashtag = models.CharField(verbose_name="Cash Tag", max_length=200, blank=True, null=True)
    
    amount = models.IntegerField(verbose_name="Amount", blank=False, null=False)


class Transaction(models.Model):
    TRANSACTION_CHOICES = [
        ("deposit", "deposit"),
        ("transfer", "transfer"),
        ("withdraw", "withdraw")
    ]
    
    ASSET_SELECTED = [
        ("Bitcoin", "Bitcoin"),
        ("Etherium", "Etherium"),
        ("BankTransfer", "BankTransfer"),
        ("Paypal", "Paypal"),
        ("CashApp", "CashApp"),
        ("usdt", "usdt")
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    custom_id = models.CharField(max_length=500, blank=True, null=True, default=random_string)
    transaction_type = models.CharField(verbose_name="Transaction Type", max_length=200, choices=TRANSACTION_CHOICES, blank=False, null=False)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    transation_state = models.BooleanField(default=False)
    selected_asset = models.CharField(verbose_name="Transaction Asset", max_length=200, choices=ASSET_SELECTED, blank=True, null=True)
    
    @property
    def assetImageURL(self):
        if self.selected_asset == "Bitcoin":
            url = "/media/images/bitcoin.png"
        elif self.selected_asset == "Etherium":
            url = "/media/images/ether.png"
        elif self.selected_asset == "BankTransfer":
            url = "/media/images/bankicon.png"
        elif self.selected_asset == "Paypal":
            url = "/media/images/paypal.png"
        elif self.selected_asset == "CashApp":
            url = "/media/images/cashapp.png"
        elif self.selected_asset == "usdt":
            url = "/media/images/usdt.png"
        else:
            url = ""
        return url
    
    def __str__(self):
        return f"{self.transaction_type.capitalize()} Transaction by {self.user.first_name}"
    

class AdminWalletAccount(models.Model):
    
    wallet_address = models.CharField(verbose_name="Wallet Address", max_length=300, blank=False, null=False)
    wallet_barcode = models.ImageField(help_text="Upload an image of your wallet Barcode", verbose_name="Wallet Barcode", upload_to='dhb/admin/')
    bank_name = models.CharField(verbose_name="Bank Name", max_length=300, blank=False, null=False)
    bank_account_name = models.CharField(verbose_name="Bank Account Name", max_length=300, blank=False, null=False)
    bank_account_number = models.IntegerField(verbose_name="Bank Account Number", blank=False, null=False)
    
    # --------- Addition Information -------- #
    etherium_value_in_dollars = models.IntegerField(default=0)
    bitcoin_value_in_dollars = models.IntegerField(default=0)
    usdt_value_in_dollars = models.IntegerField(default=0)
    
    
    def __str__(self) -> str:
        return f"Admin Datails => {self.wallet_address}"

