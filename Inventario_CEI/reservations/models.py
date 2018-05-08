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

    def get_status(self):
        return dict(self.RESERVATION_STATES).get(self.state)

    class Meta:
        abstract = True


class ArticleReservation(Reservation):
    """
    Modelo para reservas de articulos
    """
    article_or_space = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="reservations"
    )
    user = models.ForeignKey(
        RegisteredUser,
        on_delete=models.CASCADE,
        related_name="article_reservations"
    )

    def get_status(self):
        return dict(self.RESERVATION_STATES).get(self.state)

    def __str__(self):
        return "{} {} {} {}".format(
            self.user,
            self.article_or_space,
            self.initial_date,
            self.end_date
        )


class SpaceReservation(Reservation):
    """
    Modelo para reserva de espacios
    """
    article_or_space = models.ForeignKey(
        Space,
        on_delete=models.CASCADE,
        related_name="reservations"
    )
    user = models.ForeignKey(
        RegisteredUser,
        on_delete=models.CASCADE,
        related_name="space_reservations"
    )

    def __str__(self):
        return "{} {} {} {}".format(
            self.user,
            self.space,
            self.initial_date,
            self.end_date
        )


class Loan(models.Model):
    """
    Modelo para prestamos.
    """
    # ID(generado por  django)
    # user [foreign key ref Usuario]
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

    def get_status(self):
        return dict(self.LOAN_STATES).get(self.state)

    class Meta:
        abstract = True


class ArticleLoan(Loan):
    # articulo o Espacio [foreign key  ref Espacio]
    article_or_space = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="loans"
    )
    user = models.ForeignKey(
        RegisteredUser,
        on_delete=models.CASCADE,
        related_name="article_loans"
    )

    def __str__(self):
        return "{} {} {} {}".format(
            self.user,
            self.article_or_space,
            self.initial_date,
            self.end_date
        )


class SpaceLoan(Loan):
    # articulo o Espacio [foreign key  ref Espacio]
    article_or_space = models.ForeignKey(
        Space,
        on_delete=models.CASCADE,
        related_name="loans"
    )
    user = models.ForeignKey(
        RegisteredUser,
        on_delete=models.CASCADE,
        related_name="space_loans"
    )

    def get_status(self):
        return dict(self.LOAN_STATES).get(self.state)

    def __str__(self):
        return "{} {} {} {}".format(
            self.user,
            self.article,
            self.initial_date,
            self.end_date
        )
