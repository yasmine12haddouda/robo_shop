from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Product

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {
        'products': products
    })


@login_required
def seller_dashboard(request):
    # Only sellers can access the seller dashboard
    seller = getattr(request.user, 'seller', None)
    if seller is None:
        return redirect('product_list')

    # Get seller's products
    seller_products = Product.objects.filter(seller=seller)

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        price = request.POST.get('price', '0')
        stock = request.POST.get('stock', '0')
        description = request.POST.get('description', '')
        image = request.FILES.get('image')

        if name:
            Product.objects.create(
                seller=seller,
                name=name,
                price=float(price),
                stock=int(stock),
                description=description,
                image=image
            )
            return redirect('seller_dashboard')

    return render(request, 'store/seller_interface.html', {
        'seller_products': seller_products,
        'seller': seller
    })


@login_required
def add_product(request):
    # Only users with a related `Seller` may add products
    seller = getattr(request.user, 'seller', None)
    if seller is None:
        return HttpResponseForbidden('Only sellers can add products.')

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        price = request.POST.get('price', '0')
        stock = request.POST.get('stock', '0')
        description = request.POST.get('description', '')
        image = request.FILES.get('image')

        Product.objects.create(
            seller=seller,
            name=name,
            price=float(price),
            stock=int(stock),
            description=description,
            image=image
        )
        return redirect('product_list')

    return render(request, 'store/add_product.html')
