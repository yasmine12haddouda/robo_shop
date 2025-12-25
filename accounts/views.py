from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import Seller
from .forms import SignupForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data.get('role')
            user = form.save(commit=False)
            user.email = form.cleaned_data.get('email')
            user.save()

            if role == 'seller':
                Seller.objects.create(
                    user=user,
                    phone='000000000',
                    address='Algiers'
                )

            login(request, user)
            
            # Redirect sellers to seller dashboard, buyers to product list
            if role == 'seller':
                return redirect('seller_dashboard')
            return redirect('product_list')
    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            
            # Redirect sellers to seller dashboard, buyers to product list
            if hasattr(user, 'seller'):
                return redirect('seller_dashboard')
            return redirect('product_list')

        return render(request, 'accounts/login.html', {
            'error': 'البيانات غير صحيحة'
        })

    return render(request, 'accounts/login.html')


def signout(request):
    logout(request)
    return redirect('login')
