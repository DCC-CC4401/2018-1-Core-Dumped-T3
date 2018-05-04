from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.staticfiles.templatetags.staticfiles import static
# Create your models here.


class RegisteredUser(models.Model):
    '''Class that represents an user of our system.
    Fields:
        username: inherited from User 
            The RUT of the user
        password: inherited from User
            A hash of the user's password
        email: inherited from User
            The user's email
        first_name: inherited from User
            The user's first name
        last_name: inherited from User
            The user's last name
        avatar: ImageField 
            The user's profile picture
        status: PositiveSmallIntegerField
            An enumeration defining the user's status in the system.
        is_admin: boolean
            Is the user an admin.
    '''
    PRESTAMOS_RESERVAS = 0
    PRESTAMOS = 1
    RESERVAS = 2
    NADA = 3

    USER_STATES = (
        (PRESTAMOS_RESERVAS, 'Préstamos y Reservas'),
        (PRESTAMOS, 'Sólo préstamos'),
        (RESERVAS, 'Sólo reservas'),
        (NADA, 'Nada'),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    avatar = models.ImageField(
        default="users/images/default-profile.png"
    )

    status = models.PositiveSmallIntegerField(
        choices=USER_STATES,
        default=PRESTAMOS_RESERVAS
    )

    is_admin = models.BooleanField(
        default=False
    )

    def rut(self):
        counter = 0
        rut = self.user.username
        formatted_rut = ""
        for i in reversed(rut[:-1]):
            if counter != 2:
                formatted_rut += i
            else:
                formatted_rut += (i + ".")
            counter = (counter + 1) % 3
        return formatted_rut[::-1] + "-" + rut[-1]

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    print(created)
    if created:
        RegisteredUser.objects.create(user=instance)
    else:
        instance.registereduser.save()
