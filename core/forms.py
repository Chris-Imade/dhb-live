from django import forms
from .models import Account, Newsletter, ContactUs


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


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ["email",]
        widgets = {
            'email': forms.TextInput(attrs={
                'type': 'email',
                'placeholder':"Please enter your email...",
                "class": "w-full shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-l-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light", 
                'required':"", 
            }),
        }
        
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ["name", "email", "message"]
        widgets = {
            'name': forms.TextInput(attrs={
                'type': 'text',
                'placeholder':"Name",
                "class": "form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none", 
                'required':"",
                "id": "exampleInput7"
            }),
            'email': forms.TextInput(attrs={
                'type': 'email',
                'placeholder':"Email Address",
                "class": "form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none", 
                'required':"",
                "id": "exampleInput8"
            }),
            'message': forms.Textarea(attrs={
                'type': 'text',
                "class": "orm-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none", 
                'required':"",
                "id": "exampleFormControlTextarea13",
                "rows":"3",
                "placeholder":"Message",
            }),
        }
    

