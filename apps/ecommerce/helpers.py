from django.db import transaction
from djstripe.models import Customer, Price, Product
from stripe.api_resources.checkout.session import Session

from apps.users.models import CustomUser
from apps.utils.billing import get_stripe_module

from .models import Purchase


@transaction.atomic
def create_purchase_from_checkout_session(session: Session) -> Purchase:
    session_id = session.stripe_id
    client_reference_id = int(session.client_reference_id)
    user = CustomUser.objects.get(id=client_reference_id)
    if not user.customer or user.customer.id != session.customer:
        # set customer on user object for future payments
        stripe_customer = get_stripe_module().Customer.retrieve(session.customer)
        djstripe_customer = Customer.sync_from_stripe_data(stripe_customer)
        user.customer = djstripe_customer
        user.save()
    try:
        return Purchase.objects.get(checkout_session_id=session_id)
    except Purchase.DoesNotExist:
        product = Product.objects.get(id=session.line_items.data[0].price.product)
        price = Price.objects.get(id=session.line_items.data[0].price.id)
        return Purchase.objects.create(
            user=user,
            product=product,
            price=price,
            checkout_session_id=session_id,
        )
