from django.db import models
import uuid
import sys
sys.path.append('..')
from management.models import User


class Payments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    is_paid = models.BooleanField(default=False)
    token = models.TextField(max_length=128)
    date = models.DateTimeField(auto_now_add=True, blank=False)