from django.db import models
from django.db.models.fields.files import ImageField
from django.dispatch import receiver
from django.db.models.signals import post_save

from django.db.models.fields.files import ImageField
from django.dispatch import receiver
from django.db.models.signals import post_save


class Article(models.Model):
    DISPONIBLE = 0
    PRESTAMO = 1
    REPARACION = 2
    PERDIDO = 3

    ARTICLE_STATES = (
        (DISPONIBLE, "Disponible"),
        (PRESTAMO, "En préstamo"),
        (REPARACION, "En reparación"),
        (PERDIDO, "Perdido"),
    )
    
    name = models.CharField(max_length=128) # muy arbitrario
    image = models.ImageField(
        upload_to='articles/images',
        default="articles/images/default-article.jpg"
    )

    description = models.TextField()
    status = models.PositiveSmallIntegerField(
        choices=ARTICLE_STATES,
        default=DISPONIBLE
    )

    def pretty_status(self):
        return dict(self.ARTICLE_STATES).get(self.status)

    def __str__(self):
        return self.name

class Space (models.Model):
    DISPONIBLE = 0
    PRESTAMO = 1
    REPARACION = 2

    SPACE_STATES = (
        (DISPONIBLE, 'Disponible'),
        (PRESTAMO, 'En préstamo'),
        (REPARACION, 'En reparación')
    )

    name = models.CharField(
        max_length=50
    )
    
    status = models.PositiveSmallIntegerField(
        choices=SPACE_STATES,
        default=DISPONIBLE)
    
    def pretty_status(self):
        return dict(self.SPACE_STATES[self.status]).get(self.status)

    def __str__(self):
        return self.name
