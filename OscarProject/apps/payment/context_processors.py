from .models import *
from apps.customer import *
from apps.order import *


def payment_info(request):
    users = User.objects.all()
    payments = Payment.objects.all()
    purchase = Purchase.objects.all()
    print(users)
    return dict(
        users=users,
        payments = payments,
        purchase = purchase,
        )
    