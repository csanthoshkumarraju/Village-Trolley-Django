
from django.contrib import admin
from .models import Shop_Owner_Registartion

@admin.register(Shop_Owner_Registartion)
class ShopOwnerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'shop_name', 'mail_id', 'phone_number', 'city', 'state')
    search_fields = ('first_name', 'last_name', 'shop_name', 'mail_id')

