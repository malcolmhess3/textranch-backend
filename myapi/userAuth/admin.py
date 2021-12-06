from django.contrib import admin

# Register your models here.

from .models import FraudCheck, User

admin.site.register(User)
admin.site.register(FraudCheck)