from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.forms import MyPassWordChangeForm, UserEditForm
from core.forms import AccountDetailsEditForm, NewsletterForm, ContactForm
from django.contrib.auth import update_session_auth_hash
from core.models import Transaction, Withdrawal, AdminWalletAccount, Transfer
from django.contrib import messages
import json
import ast

# Create your views here.
def home(request):
    form = NewsletterForm()
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Newsletter request was submitted successfully. Thank you!")
            return redirect("home")
    return render(request, 'index.html', {
        "form": form
    })


def about(request):
    form = NewsletterForm()
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Newsletter request was submitted successfully. Thank you!")
            return redirect("about")
    return render(request, 'about.html', {
        "form": form
    })

def contact(request):
    newsletter_form = NewsletterForm()
    contact_form = ContactForm()
    if request.method == 'POST' and "sendNewsLetter" in request.POST:
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            messages.success(request, "Newsletter request was submitted successfully. Thank you!")
            return redirect("contact")
        
    elif request.method == 'POST' and 'sendContactMessage' in request.POST:
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, "Thank you for reaching out. A member of our team will get back to you... ")
            return redirect("contact")
    return render(request, 'contact.html', {"newsletter_form": newsletter_form, "contact_form": contact_form})

@login_required(login_url="login")
def dashboard(request):
    transactions = Transaction.objects.filter(user=request.user)
    transaction_count = Transaction.objects.filter(user=request.user).count()

    transaction_deposits_accepted = Transaction.objects.filter(
        user=request.user, 
        transaction_type="deposit", 
        transaction_state=True
    )
    # Generate ransomeware code in python 
    withdrawal = Withdrawal.objects.filter(user=request.user)
    withdrawal_count = Withdrawal.objects.filter(user=request.user).count()
    
    total_for_deposits = 0
    for deposit in transaction_deposits_accepted:
        total_for_deposits += deposit.amount

    return render(request, 'dashboard/dashboard.html', {
        "transactions":transactions,
        "transaction_count":transaction_count,
        "withdrawal": withdrawal,
        "withdrawal_count": withdrawal_count,
        "transaction_deposits": transaction_deposits_accepted,
        "total_for_deposits": total_for_deposits,

    })



@login_required(login_url="login")
def settings(request):
    password_change_form = MyPassWordChangeForm(user=request.user)
    user_data_form = UserEditForm(instance=request.user)
    user_account_form = AccountDetailsEditForm(instance=request.user.account)
    
    if request.method == 'POST' and 'UserPersonalDataBtn' in request.POST:
        user_data_form = UserEditForm(request.POST, request.FILES, instance=request.user)
        if user_data_form.is_valid():
            user_data_form.save()
            return redirect('settings')
    if request.method == 'POST' and 'PasswordChangeBtn' in request.POST:
        password_change_form = MyPassWordChangeForm(user=request.user, data=request.POST)
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully')
            return redirect('settings')
        else:
            messages.error(request, 'Inconsistent password')
            return redirect('settings')
        
    if request.method == 'POST' and 'UserAccountBtn' in request.POST:
        user_account_form = AccountDetailsEditForm(request.POST, instance=request.user.account)
        if user_account_form.is_valid():
            user_account_form.save()
            messages.success(request, 'Bank info updated successfully')
            return redirect('settings')
        else:
            messages.error(request, 'A problem was encountered updated your bank info. Try again.')
        
    context = {
        "password_change_form": password_change_form,
        "personal_form": user_data_form,
        "user_account_form": user_account_form
        
    }
    
    return render(request, 'dashboard/settings.html', context)

@login_required(login_url="login")
def deposit(request):
    admin_details = AdminWalletAccount.objects.last()
    
    context = {"admin_details": admin_details}
    return render(request, 'dashboard/deposit.html', context)


@login_required(login_url="login")
def history(request):
    transactions = Transaction.objects.filter(user=request.user)
    
    context = {
        "transactions": transactions
    }
    return render(request, 'dashboard/history.html', context)

@login_required(login_url="login")
def withdraw(request):
    if request.method == 'POST':
        cash_balance = request.POST.get('cash_balance', None)
        change_payment_details = request.POST.get('changePaymentDetails', None)
        wallet_address = request.POST.get('wallet_address', None)
        account_number = request.POST.get('account_number', None)
        account_name = request.POST.get('account_name', None)
        bank_name = request.POST.get('bank_name', None)
        swift_code = request.POST.get('swift_code', None)
        paypal_email = request.POST.get('paypal_email', None)
        cashtag = request.POST.get('cashtag', None)
        amount = request.POST.get('amount', None)

        withdrawal = Withdrawal(
            user=request.user,
            balance_type=cash_balance,
            selected_asset=change_payment_details,
            ethereum_address=wallet_address,
            bitcoin_address=wallet_address,
            account_name=account_name,
            account_number=account_number,
            bank_name=bank_name,
            swift_code=swift_code,
            paypal_email=paypal_email,
            cashtag=cashtag,
            amount=amount
        )
        withdrawal.save()
        transaction = Transaction(
            user=request.user, 
            transaction_type="withdraw", 
            selected_asset=change_payment_details, 
            amount=amount
        )
        transaction.save()
        messages.success(request, "Your transaction is being processed. A confirmation mail will be sent to you upon confirmation.")
        return redirect("history")

    context = {'user_balance': request.user.balance}
    return render(request, 'dashboard/withdraw.html', context)

@login_required(login_url="login")
def transfer(request):
    if request.method == 'POST':
        cash_balance = request.POST.get('cash_balance', None)
        change_payment_details = request.POST.get('changePaymentDetails', None)
        wallet_address = request.POST.get('wallet_address', None)
        account_number = request.POST.get('account_number', None)
        account_name = request.POST.get('account_name', None)
        bank_name = request.POST.get('bank_name', None)
        swift_code = request.POST.get('swift_code', None)
        paypal_email = request.POST.get('paypal_email', None)
        cashtag = request.POST.get('cashtag', None)
        amount = request.POST.get('amount', None)

        withdrawal = Transfer(
            user=request.user,
            balance_type=cash_balance,
            selected_asset=change_payment_details,
            ethereum_address=wallet_address,
            bitcoin_address=wallet_address,
            account_name=account_name,
            account_number=account_number,
            bank_name=bank_name,
            swift_code=swift_code,
            paypal_email=paypal_email,
            cashtag=cashtag,
            amount=amount
        )
        withdrawal.save()
        transaction = Transaction(
            user=request.user, 
            transaction_type="transfer", 
            selected_asset=change_payment_details, 
            amount=amount
        )
        transaction.save()
        messages.success(request, "Your transaction is being processed. A confirmation mail will be sent to you upon confirmation.")
        return redirect("history")
    context = {'user_balance': request.user.balance}
    return render(request, 'dashboard/transfer.html', context)


