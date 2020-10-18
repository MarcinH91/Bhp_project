from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views import View
from shopping_cart.models import Order, OrderItem, Address
from core.models import Product
from shopping_cart.forms import CheckoutForm


def is_valid_form(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid


@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_queryset = Order.objects.filter(user=request.user, is_ordered=False)
    if order_queryset.exists():
        order = order_queryset[0]
        if order.items.filter(item__slug=item.slug).exists():
            messages.info(request, 'Ten produkt znajduje się już w koszyku')
            return redirect('/')
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date
        )
    order.items.add(order_item)
    messages.info(request, 'Produkt został dodany do koszyka')
    return redirect('/')


@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_queryset = Order.objects.filter(
        user=request.user,
        is_ordered=False
    )
    if order_queryset.exists():
        order = order_queryset[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect("shopping_cart:cart")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("/")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("/")


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, is_ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'cart.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return render(self.request, 'cart.html')


class CheckoutView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, is_ordered=False)
            form = CheckoutForm()
            context = {
                'form': form,
                'order': order,
            }

            billing_address_qs = Address.objects.filter(
                user=self.request.user,
                default=True
            )
            if billing_address_qs.exists():
                context.update(
                    {'default_billing_address': billing_address_qs[0]})
            return render(self.request, "checkout.html", context)
        except ObjectDoesNotExist:
            messages.info(self.request, "Brak aktywnego zamówienia")
            return redirect("/")

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user, is_ordered=False)
            if form.is_valid():
                use_default_billing = form.cleaned_data.get(
                    'use_default_billing')

                if use_default_billing:
                    address_qs = Address.objects.filter(
                        user=self.request.user,
                        default=True
                    )
                    if address_qs.exists():
                        billing_address = address_qs[0]
                        order.billing_address = billing_address
                        order.save()
                    else:
                        messages.info(
                            self.request, "No default billing address available")
                        return redirect('shopping_cart:checkout')
                else:
                    billing_address1 = form.cleaned_data.get(
                        'billing_address')
                    billing_country = form.cleaned_data.get(
                        'billing_country')
                    billing_zip = form.cleaned_data.get('billing_zip')
                    billing_city = form.cleaned_data.get('billing_city')

                    if is_valid_form([billing_address1, billing_country, billing_zip, billing_city]):
                        billing_address = Address(
                            user=self.request.user,
                            street_address=billing_address1,
                            country=billing_country,
                            zip=billing_zip,
                            city=billing_city
                        )
                        billing_address.save()

                        order.billing_address = billing_address
                        order.save()

                        set_default_billing = form.cleaned_data.get(
                            'set_default_billing')
                        if set_default_billing:
                            billing_address.default = True
                            billing_address.save()

                    else:
                        messages.info(
                            self.request, "Please fill in the required billing address fields")

                payment_option = form.cleaned_data.get('payment_option')

                if payment_option == 'B':
                    return redirect('/', payment_option='blik')
                elif payment_option == 'P':
                    return redirect('/', payment_option='paypal')
                elif payment_option == 'O':
                    return redirect('/', payment_option='transfer')
                elif payment_option == 'K':
                    return redirect('/', payment_option='card')
                else:
                    messages.warning(
                        self.request, "Invalid payment option selected")
                    return redirect('shopping_cart:checkout')
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/")




