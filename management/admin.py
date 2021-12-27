from django.contrib import admin
from . import models

from rest_framework.authtoken.models import Token

# from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User)
admin.site.register(models.SMSVerification)

admin.site.register(models.Withdraw)
admin.site.register(models.ChargePlaceHolder)
admin.site.register(models.Stream)
admin.site.register(models.Roles)