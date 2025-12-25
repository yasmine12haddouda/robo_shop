from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from django.contrib.auth.decorators import login_required


@login_required
def add_to_cart(request, product_id):
    # prevent sellers from using buyer cart endpoints
    if hasattr(request.user, 'seller'):
        return redirect('home')

    if request.method != 'POST':
        return redirect('product_list')

    product = get_object_or_404(Product, id=product_id)

    try:
        qty = int(request.POST.get('quantity', 1))
    except (TypeError, ValueError):
        qty = 1

    if qty < 1:
        qty = 1

    cart = request.session.get('cart', {})
    key = str(product_id)
    current = cart.get(key, 0)

    # Do not let cart quantity exceed available stock
    allowed = max(0, product.stock - current)
    add_qty = min(qty, allowed)
    if add_qty <= 0:
        # nothing to add (out of stock or already at max) — show cart
        request.session['cart'] = cart
        return redirect('view_cart')

    cart[key] = current + add_qty
    request.session['cart'] = cart
    return redirect('view_cart')


@login_required
def view_cart(request):
    if hasattr(request.user, 'seller'):
        return redirect('home')

    cart = request.session.get('cart', {})
    products = []
    total = 0

    for product_id_str, quantity in cart.items():
        product = get_object_or_404(Product, id=int(product_id_str))
        product.quantity = quantity
        product.total_price = product.price * quantity
        total += product.total_price
        products.append(product)

    return render(request, 'shopping_cart/cart.html', {'products': products, 'total': total})


@login_required
def remove_from_cart(request, product_id):
    if hasattr(request.user, 'seller'):
        return redirect('home')

    cart = request.session.get('cart', {})
    key = str(product_id)
    if key in cart:
        del cart[key]
        request.session['cart'] = cart
    return redirect('view_cart')
