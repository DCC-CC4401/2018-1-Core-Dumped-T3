from django.db import models
from django.db.models.fields.files import ImageField


# Create your models here.
class AbstractInventory(models.Model):
    class Meta:
        abstract = True


class Article(AbstractInventory):
    DISPONIBLE = 0
    PRESTAMO = 1
    REPARACION = 2
    PERDIDO = 3

    ARTICLE_STATES =  (
        (DISPONIBLE, "Disponible"),
        (PRESTAMO, "En préstamo"),
        (REPARACION, "En reparación"),
        (PERDIDO, "Perdido"),
    )
    
    name = models.CharField(max_length=128) # muy arbitrario
    image = models.ImageField()
    description = models.TextField()
    status = models.PositiveSmallIntegerField(
        choices=ARTICLE_STATES,
        default=DISPONIBLE
    )

    def pretty_status(self):
        return self.ARTICLE_STATES[self.status][1]

    def __str__(self):
        return self.name


class Space (AbstractInventory):
    name = models.CharField(
        max_length=50
    )
    DISPONIBLE = 0
    PRESTAMO = 1
    REPARACION = 2

    SPACE_STATUS = (
        (DISPONIBLE, 'disponible'),
        (PRESTAMO, 'en prestamo'),
        (REPARACION, 'en reparacion')
    )

    status = models.PositiveSmallIntegerField(
        choices=SPACE_STATUS,
        default=0)
