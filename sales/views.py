from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from .models import Payment, Order

# Algerian states (wilayas)
ALGERIAN_STATES = [
    'Adrar','Chlef','Laghouat','Oum El Bouaghi','Batna','Béjaïa','Biskra','Béchar','Blida','Bouira',
    'Tamanrasset','Tébessa','Tlemcen','Tiaret','Tizi Ouzou','Algiers','Djelfa','Jijel','Sétif','Saïda',
    'Skikda','Sidi Bel Abbès','Annaba','Guelma','Constantine','Médéa','Mostaganem','MSila','Mascara','Ouargla',
    'Oran','El Bayadh','Illizi','Bordj Bou Arréridj','Boumerdès','El Tarf','Tindouf','Tissemsilt','El Oued','Khenchela',
    'Souk Ahras','Tipaza','Mila','Aïn Defla','Naâma','Aïn Témouchent','Ghardaïa','Relizane'
]

def home(request):
    return render(request, 'sales/home.html')


def checkout(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0
    for product_id_str, quantity in cart.items():
        product = get_object_or_404(Product, id=int(product_id_str))
        total += product.price * quantity
        products.append(product)

    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        phone = request.POST.get('phone', '').strip()
        state = request.POST.get('state', '').strip()
        payment_method = request.POST.get('payment_method', '')

        # Basic validation
        if not (first_name and last_name and phone and state):
            return render(request, 'sales/checkout.html', {
                'error': 'الرجاء ملء كل الحقول المطلوبة',
                'total': total,
                'states': ALGERIAN_STATES
            })

        Payment.objects.create(
            user=request.user if request.user.is_authenticated else None,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            state=state,
            amount=total,
            payment_method=payment_method
        )

        # Clear cart
        request.session['cart'] = {}

        return redirect('payment_success')

    return render(request, 'sales/checkout.html', {'total': total, 'states': ALGERIAN_STATES})


def payment_success(request):
    return render(request, 'sales/success.html')
