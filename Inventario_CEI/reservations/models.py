# Django
from django.db import models
from django.utils import timezone
import datetime
# Models
from articles.models import Article, Space
from users.models import RegisteredUser
# Create your models here.


class Reservation(models.Model):
    """
    Modelo para reservas.
    """
    # ID(generado por  django)
    # RUT[foreign key ref Usuario]

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="reservations",
        null=True,
        blank=True
    )
    space = models.ForeignKey(
        Space,
        on_delete=models.CASCADE,
        related_name="reservations",
        null=True,
        blank=True
    )
    user = models.ForeignKey(
        RegisteredUser,
        on_delete=models.CASCADE,
        related_name="reservations"
    )
    is_article = models.BooleanField(
        default=False
    )
    is_space = models.BooleanField(
        default=False
    )

    # Fecha Inicio[Datetime]
    initial_date = models.DateTimeField(
        verbose_name="initial date",
        default=timezone.now
    )
    # Fecha Término[Datetime]
    end_date = models.DateTimeField(
        verbose_name="end date",
        default=timezone.now
    )
    PENDIENTE = 0
    ENTREGADO = 1
    RECHAZADO = 2

    RESERVATION_STATES = (
        (PENDIENTE, 'pendiente'),
        (ENTREGADO, 'entregado'),
        (RECHAZADO, 'rechazado'),
    )
    
    state = models.PositiveSmallIntegerField(
        choices=RESERVATION_STATES,
        default=PENDIENTE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def get_status(self):
        return dict(self.RESERVATION_STATES).get(self.state)

    def __str__(self):
        if self.is_article:
            return "{} {} {} {}".format(
                self.user,
                self.article,
                self.initial_date,
                self.end_date
            )
        if self.is_space:
            return "{} {} {} {}".format(
                self.user,
                self.space,
                self.initial_date,
                self.end_date
            )

    class Meta:
        verbose_name = 'reservation',
        verbose_name_plural = 'reservations'


class Loan(models.Model):
    """
    Modelo para prestamos.
    """
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="loans",
        null=True,
        blank=True
    )
    space = models.ForeignKey(
        Space,
        on_delete=models.CASCADE,
        related_name="loans",
        null=True,
        blank=True
    )
    user = models.ForeignKey(
        RegisteredUser,
        on_delete=models.CASCADE,
        related_name="loans"
    )
    is_article = models.BooleanField(
        default=False
    )
    is_space = models.BooleanField(
        default=False
    )
    # Fecha Inicio[Datetime]
    initial_date = models.DateTimeField(
        verbose_name="initial date",
        default=timezone.now
    )
    # Fecha Término[Datetime]
    end_date = models.DateTimeField(
        verbose_name="end date",
        default=timezone.now
    )
    VIGENTE = 0
    CADUCADO = 1
    RECIBIDO = 2
    PERDIDO = 3

    LOAN_STATES = (
        (VIGENTE, 'vigente'),
        (CADUCADO, 'caducado'),
        (RECIBIDO, 'recibido'),
        (PERDIDO, 'perdido'),
    )
    state = models.PositiveSmallIntegerField(
        choices=LOAN_STATES,
        default=VIGENTE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    created_by = models.ForeignKey(
        RegisteredUser,
        on_delete=models.CASCADE,
        related_name="accepted_loans"
    )

    def get_status(self):
        return dict(self.LOAN_STATES).get(self.state)

    def __str__(self):
        if self.is_article:
            return "{} {} {} {}".format(
                self.user,
                self.article,
                self.initial_date,
                self.end_date
            )
        if self.is_space:
            return "{} {} {} {}".format(
                self.user,
                self.space,
                self.initial_date,
                self.end_date
            )

    class Meta:
        verbose_name = 'loan',
        verbose_name_plural = 'loans'
