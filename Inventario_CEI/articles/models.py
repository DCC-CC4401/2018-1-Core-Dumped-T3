from django.db import models

# Create your models here.
class Article(models.Model):
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