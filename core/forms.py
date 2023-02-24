from django import forms
from .models import Account


class AccountDetailsEditForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            'account_number',
            'account_name',
            'bank_name',
            'bitcoin_address',
            'etherium_address',
            'cashtag',
            'paypal_email',
            'swift_code'
        ]
        
        widgets = {
            'account_number': forms.TextInput(attrs={
                'type': 'account_number',
                'class': 'form-control', 
                'id':"exampleFormControlInput1", 
            }),
            'account_name': forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control', 
                'id':"exampleFormControlInput1", 
            }),
            'bank_name': forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control', 
                'id':"exampleFormControlInput1", 
            }),
            'bitcoin_address': forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control', 
                'id':"exampleFormControlInput1", 
            }),
            'etherium_address': forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id':"exampleFormControlInput1",
            }),
            'cashtag': forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control', 
                'id':"exampleFormControlInput1", 
            }),
            'paypal_email': forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control', 
                'id':"exampleFormControlInput1",
            }),
            'swift_code': forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control', 
                'id':"exampleFormControlInput1",
            }),
        }




