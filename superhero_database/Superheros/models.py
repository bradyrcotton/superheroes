from django.db import models
# Create your models here.


class Superhero(models.Model):
    name = models.CharField(max_length=50)
    universe = models.CharField(max_length=50)
    powers = models.CharField(max_length=50)

    def __str__(self):
        return self.name
