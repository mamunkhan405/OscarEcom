from oscar.apps.payment.admin import *  # noqa
from apps.payment.models import *  # noqa
from django.contrib import admin

admin.site.register(Payment)
