from django.db import models


class NatureChoices(models.TextChoices):
    IN = "Entrada"
    OUT = "Saída"


class Type(models.Model):
    class Meta:
        ordering = ("id",)

    type = models.CharField(max_length=1)
    description = models.CharField(max_length=120)
    nature = models.CharField(
        max_length=24,
        choices=NatureChoices.choices,
        default=NatureChoices.IN,
    )
