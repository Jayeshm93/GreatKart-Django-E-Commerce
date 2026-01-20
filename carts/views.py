from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product, Variation
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)  # Get product

    product_variation = []
    if request.method == 'POST':
        for item in request.POST:
            key = item
            value = request.POST[key]

            try:
                variation = Variation.objects.get(product=product, variation_category__iexact=key,
                                                  variation_value__iexact=value)
                product_variation.append(variation)
            except:
                pass

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))  # get cart using cart_id
    except Cart.DoesNotExist:
        # Create cart id, if not exist
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
    cart.save()

    # Check product exist in cart or not
    is_cart_item_exists = CartItem.objects.filter(product=product, cart=cart).exists()
    if is_cart_item_exists:
        cart_item = CartItem.objects.filter(product=product, cart=cart)

        exist_var_list = []
        ids = []
        for item in cart_item:
            existing_variation = item.variations.all()
            exist_var_list.append(list(existing_variation))
            ids.append(item.id)  # CartItem id

        # Check curr variation is exist in added cart product
        if product_variation in exist_var_list:
            idx = exist_var_list.index(product_variation)
            item_id = ids[idx]  # Get specific existed variation CartItem id to increases the qty
            item = CartItem.objects.get(product=product, id=item_id)
            item.quantity += 1  # Existing product variation -> increment qty
            item.save()
        else:
            # Create CartItem, if not exist - same 'product variations' in cart
            item = CartItem.objects.create(product=product, quantity=1, cart=cart)
            # Add variation for that specific product
            if len(product_variation) > 0:
                item.variations.clear()
                item.variations.add(*product_variation)
            item.save()
    else:
        # Create CartItem if not 'exist product in cart'
        cart_item = CartItem.objects.create(product=product, quantity=1, cart=cart)
        # Add variation for that specific product
        if len(product_variation) > 0:
            cart_item.variations.clear()
            cart_item.variations.add(*product_variation)
        cart_item.save()
    return redirect('cart')  # And redirect on cart page


def remove_cart(request, product_id, cart_item_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)  # Get specific prod from this cart
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except:
        pass
    return redirect('cart')


def remove_cart_item(request, product_id, cart_item_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)  # Get specific prod from this cart
    cart_item.delete()
    return redirect('cart')


def cart(request, total=0, quantity=0, cart_items=None):
    try:
        tax = 0
        grand_total = 0

        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity

        # 2% tax taken
        tax = (total * (2/100))
        grand_total = total + tax

    except ObjectDoesNotExist:
        pass

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
    }

    return render(request, 'store/cart.html', context)
