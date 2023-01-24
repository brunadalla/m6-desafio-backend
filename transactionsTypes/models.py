from django.db import models


class NatureChoices(models.TextChoices):
    IN = "In"
    OUT = "Out"


class Type(models.Model):
    class Meta:
        ordering = ("id",)

    description = models.CharField(max_length=120)
    nature = models.CharField(
        max_length=3,
        choices=NatureChoices.choices,
        default=NatureChoices.IN,
    )
