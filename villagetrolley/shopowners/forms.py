# forms.py
from django import forms
from django.core.validators import EmailValidator, RegexValidator
from django.core.exceptions import ValidationError
from .models import Shop_Owner_Registartion

def validate_password_strength(value):
    min_length = 8  # Minimum password length

    if len(value) < min_length:
        raise ValidationError(
            f"The password must be at least {min_length} characters long."
        )
    if not any(char.isupper() for char in value):
        raise ValidationError("The password must contain at least one uppercase letter.")
    if not any(char.islower() for char in value):
        raise ValidationError("The password must contain at least one lowercase letter.")
    if not any(char.isdigit() for char in value):
        raise ValidationError("The password must contain at least one digit.")
    if not any(char in "!@#$%^&*()_+{}[];:,.<>?/~`" for char in value):
        raise ValidationError("The password must contain at least one special character.")

class ShopOwnerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Shop_Owner_Registartion
        fields = [
            'first_name', 'last_name', 'shop_name', 'mail_id', 
            'phone_number', 'street_address', 'village', 
            'mandal', 'city', 'state', 'zip_pin_code', 'password'
        ]

    def __init__(self, *args, **kwargs):
        super(ShopOwnerRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': 'First name'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Last name'})
        self.fields['shop_name'].widget.attrs.update({'placeholder': 'Shop name'})
        self.fields['mail_id'].widget.attrs.update({'placeholder': 'Email ID'})
        self.fields['phone_number'].widget.attrs.update({'placeholder': '10 digit Phone Number'})
        self.fields['street_address'].widget.attrs.update({'placeholder': 'Street Address'})
        self.fields['village'].widget.attrs.update({'placeholder': 'Village name'})
        self.fields['mandal'].widget.attrs.update({'placeholder': 'Mandal name'})
        self.fields['city'].widget.attrs.update({'placeholder': 'City Name'})
        self.fields['state'].widget.attrs.update({'placeholder': 'State Name'})
        self.fields['zip_pin_code'].widget.attrs.update({'placeholder': 'Pin Code'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Enter Your Password'})
