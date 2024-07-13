# myapp/urls.py
from django.urls import path,include

from . import views
from django.views.i18n import set_language
urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('additems', views.additems, name='additems'),
    path('billingform', views.billingform, name='billingform'),
    path('analytics', views.analytics, name='analytics'),
    path('lowstockproducts', views.lowstock, name='lowstock'),
    path('nearbystores', views.nearbystores, name='nearbystores'),
    path('shopproducts', views.shopproducts, name='shopproducts'),
    path('knowmore', views.knowmore, name='knowmore'),
    path('daily_monthly_data', views.daily_monthly_data, name='daily_monthly_data'),
    path('resetpwd', views.resetpwd, name='resetpwd'),
    path('custdmhist', views.custdmhist, name='custdmhist'),
    path('customer_register', views.customer_register, name='customer_register'),
    path('customer_login', views.customer_login, name='customer_login'),
    path('common_reg_login', views.common_reg_login, name='common_reg_login'),
 
]


