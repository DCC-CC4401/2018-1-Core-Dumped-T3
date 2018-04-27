# Django
from django.db import models
import datetime
# Models

# Enum
from .enums import *
# Create your models here.


class Reservation(models.Model):
    """
    Modelo para reservas.
    """
    # ID(generado por  django)
    # RUT[foreign key ref Usuario]
    #user = models.ForeignKey()
    # Espacio[foreign key  ref Espacio]
    #article_or_space = models.ForeignKey()
    # Fecha Inicio[Datetime]
    initial_date = models.DateTimeField(
        verbose_name="initial date",
        default=datetime.datetime.now()
    )
    # Fecha Término[Datetime]
    end_date = models.DateTimeField(
        verbose_name="end date",
        default=datetime.datetime.now()
    )
    state = models.IntegerField(
        choices=ReservationEnum.RESERVATION_STATES,
        default=ReservationEnum.PENDIENTE
    )

    def __str__(self):
        return "{} {} {} {}".format(
            "user",#self.user,
            "article",#self.article_or_space,
            self.initial_date,
            self.end_date
        )


class Loan(models.Model):
    """
    Modelo para prestamos.
    """
    # ID(generado por  django)
    # user [foreign key ref Usuario]
    #user = models.ForeignKey()
    # articulo o Espacio [foreign key  ref Espacio]
    #article_or_space = models.ForeignKey()
    # Fecha Inicio[Datetime]
    initial_date = models.DateTimeField(
        verbose_name="initial date",
        default=datetime.datetime.now()
    )
    # Fecha Término[Datetime]
    end_date = models.DateTimeField(
        verbose_name="end date",
        default=datetime.datetime.now()
    )
    state = models.IntegerField(
        choices=LoanEnum.LOAN_STATES,
        default=LoanEnum.VIGENTE
    )

    def __str__(self):
        return "{} {} {} {}".format(
            "user",#self.user,
            "article",#self.article_or_space,
            self.initial_date,
            self.end_date
        )
