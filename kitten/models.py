from django.db import models


class Kitten(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    cuteness = models.BooleanField()
    softness = models.BooleanField()

    def __str__(self):
        return self.name
