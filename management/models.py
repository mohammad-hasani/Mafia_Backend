import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.TextField(max_length=14, default=0)
    money = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    score = models.IntegerField(default=0, null=False, blank=False)
    rank = models.IntegerField(default=0, null=False, blank=False)
    is_admin = models.BooleanField(default=0, null=False, blank=False)

    class Meta:
        db_table = 'auth_user'


class SMSVerification(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    phone_number = models.TextField(max_length=14)
    verification_code = models.TextField(max_length=6)
    date = models.DateTimeField(auto_now_add=True, blank=False)


class Withdraw(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=256)
    card_number = models.TextField(max_length=16, blank=False, null=False)
    money = models.DecimalField(max_digits=10, decimal_places=3, default=0)


class Discount(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.TextField(max_length=10)
    amount = models.IntegerField()


class ChargePlaceHolder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    charge = models.IntegerField()


class Stream(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stream = models.TextField(max_length=256)


class Roles(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(max_length=30)


class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(max_length=256)
    avatar = models.TextField(max_length=256)
    Role = models.ForeignKey(Roles, on_delete=models.CASCADE)


class GameChosenRoles(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class GameState(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()