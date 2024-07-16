from django.db import models
from django.core.validators import EmailValidator, RegexValidator
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


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


class Shop_Owner_Registartion(models.Model):
    first_name = models.CharField(max_length=200,null=False, blank=False)
    last_name = models.CharField(max_length=200,null=False, blank=False)
    shop_name = models.CharField(max_length=1000,null=False, blank=False)
    mail_id = mail_id = models.CharField(
        max_length=100,
        validators=[
            EmailValidator(message=_('Enter a valid email address.')),
            RegexValidator(
                regex=r'^[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}$',
                message=_('Enter a valid email address.'),
                code='invalid_email'
            ),
        ],
        null=False,
        blank=False,
        unique=True
        )
      
    phone_number = models.IntegerField(
            max_length=10,  
            validators=[
                MinLengthValidator(10, message=_('Phone number must be at least 10 digits.')),
                MaxLengthValidator(10, message=_('Phone number cannot be more than 10 digits.')),
            ],
            unique=True, 
            verbose_name=_('Phone Number'),
            null=False,
            blank=False, 
        )
    street_address = models.CharField(max_length=500,null=False,blank=False)
    village = models.CharField(max_length=500,null=False,blank=False)
    mandal = models.CharField(max_length=500,null=False,blank=False)
    city = models.CharField(max_length=500,null=False,blank=False)
    state = models.CharField(max_length=500,null=False,blank=False)
    zip_pin_code = models.IntegerField(blank=False, null=False)
    password = models.CharField(max_length=100, validators=[validate_password_strength])

    def __str__(self):
        return self.Shop_Owner_Registartion.first_name



