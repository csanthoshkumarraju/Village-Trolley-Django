from django.shortcuts import render, redirect
from .forms import ShopOwnerRegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def customer_registration_form(request):
    form = UserCreationForm()
    return render(request, 'register.html', {'form': form})






# def register(request):
#     if request.method == 'POST':
#         form = ShopOwnerRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Registration successful!')
#             return redirect('login')  
#     else:
#         form = ShopOwnerRegistrationForm()
    
#     return render(request, 'register.html', {'form': form})

