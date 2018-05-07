from django.db import models


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
        upload_to='articles'
    )
    description = models.TextField()
    status = models.PositiveSmallIntegerField(
        choices=ARTICLE_STATES,
        default=DISPONIBLE
    )

    def pretty_status(self):
        return self.ARTICLE_STATES[self.status][1]

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
        return self.SPACE_STATES[self.status][1]

    def __str__(self):
        return self.name
