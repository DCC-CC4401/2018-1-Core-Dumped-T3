from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class RegisteredUser(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    RUT = models.CharField(
        max_length=9
    )
    email = models.EmailField()
    can_reserve = models.BooleanField(
        default=True
    )
    is_admin = models.BooleanField(
        default=False
    )

