from django.db import models

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
        upload_to='articles',
        default="articles/images/items/"
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

@receiver(post_save, sender=Article)
def create_article(sender, instance, created, **kwargs):
    if(created):
        instance.image = str(instance.image) + str(instance.id) + ".png"
        instance.save()

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
