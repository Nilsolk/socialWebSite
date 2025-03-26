from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, Order, OrderItem
from django.contrib.auth.decorators import login_required

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('catalog:product_list')

@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    if not cart_items.exists():
        return redirect('catalog:product_list')
    
    order = Order.objects.create(user=request.user, total_price=0)
    total_price = 0
    
    for item in cart_items:
        OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity, price=item.product.price)
        total_price += item.product.price * item.quantity
    
    order.total_price = total_price
    order.save()
    cart_items.delete()
    
    return redirect('catalog:order_success')

def order_success(request):
    return render(request, 'order_success.html')

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).prefetch_related('items__product')
    return render(request, 'orders.html', {'orders': orders})
