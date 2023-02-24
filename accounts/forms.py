
from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm


class UserFormCreate(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super(UserFormCreate, self).__init__(*args, **kwargs)
        
        """ FOR password1 field """
        self.fields['password1'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['password1'].widget.attrs['type'] = 'password'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].widget.attrs['name'] = 'password1'
        self.fields['password1'].widget.attrs['id'] = 'exampleInputPassword'



        """ FOR password2 field """
        self.fields['password2'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['password2'].widget.attrs['type'] = 'password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Password Confirmation'
        self.fields['password2'].widget.attrs['name'] = 'password2'
        self.fields['password2'].widget.attrs['id'] = 'exampleRepeatPassword'

    class Meta:
        model = User
        fields = [
            'email', 
            'username',
            'first_name', 
            'last_name', 
            'address',
            'country',
            'phone_number',
            'password1',
            'password2',
        ]
        widgets = {
            'email': forms.TextInput(attrs={
                'type': 'email',
                'class': 'form-control', 
                'placeholder': 'Email',
            }),
            'username': forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control', 
                'placeholder': 'Username',
            }),
            'first_name': forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'First Name',
            }),
            'last_name': forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Last Name',
            }),
            'address': forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Address',
            }),
            'phone_number': forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Phone Number',
            }),

            'country': forms.Select(attrs={
                'class': 'js-example-basic-single form-control w-100',
                'style': "width: 100%;",
            }),
		}
        



class MyPassWordChangeForm(PasswordChangeForm):

	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user')
		print(user)

		super(MyPassWordChangeForm, self).__init__(user, *args, **kwargs)
		
		self.fields['old_password'].widget.attrs['class'] = 'form-control'
		self.fields['old_password'].widget.attrs['id'] = 'exampleFormControlInput1'
		self.fields['old_password'].widget.attrs['type'] = 'password'


		self.fields['new_password1'].widget.attrs['class'] = 'form-control'
		self.fields['new_password1'].widget.attrs['id'] = 'exampleFormControlInput2'
		self.fields['new_password1'].widget.attrs['type'] = 'password'

		self.fields['new_password2'].widget.attrs['class'] = 'form-control'
		self.fields['new_password2'].widget.attrs['id'] = 'exampleFormControlInput3'
		self.fields['new_password2'].widget.attrs['type'] = 'password'


	class Meta:
		model = User
		fields = '__all__'




class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'phone_number',
            'country',
            'address',
            'image',
            'first_name',
            'last_name',
            'gender'
        ]
        widgets = {
            'email': forms.TextInput(attrs={
                'type': 'email',
                'class': 'form-control', 
                'placeholder': 'Email',
                'id':"exampleFormControlInput1", 
                'placeholder':"name@example.com"
            }),
            'gender': forms.Select(attrs={
                'class': 'js-example-basic-single form-control w-100',
                'style': "width: 100%;",
                "id":"exampleFormControlInput1"
            }),
            'username': forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control', 
                'placeholder': 'Username',
                'id':"exampleFormControlInput1", 
                'placeholder':"@yourusername"
            }),
            'first_name': forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'First Name',
            }),
            'last_name': forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Last Name',
            }),
            'address': forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Address',
            }),
            'phone_number': forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': '+499 545 7642 094',
                'id': 'exampleFormControlInput1'
            }),

            'country': forms.Select(attrs={
                'class': 'js-example-basic-single form-control w-100',
                'style': "width: 100%;",
                "id":"exampleFormControlInput1"
            }),
		}

