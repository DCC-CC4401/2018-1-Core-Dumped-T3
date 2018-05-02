from django.db import models


# Create your models here.
class AbstractInventory(models.Model):
    class Meta:
        abstract = True


class Article(AbstractInventory):
    name = models.CharField(max_length=128) # muy arbitrario
    image = models.BinaryField()
    description = models.TextField()
    status = models.PositiveSmallIntegerField(default=0)

    def pretty_status(self):
        return {
            0: "Disponible",
            1: "En préstamo",
            2: "En reparación",
            3: "Perdido",
        }.get(self.status, "Desconocido")

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
