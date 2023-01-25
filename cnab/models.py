import uuid
from django.db import models


class Cnab(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    cpf = models.TextField(max_length=11)
    date = models.DateField()
    card = models.TextField(max_length=12)
    time = models.TimeField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.TextField()
    store = models.TextField()
    type_number = models.TextField(max_length=1)

    type = models.ForeignKey(
        "transactionsTypes.Type",
        on_delete=models.CASCADE,
        related_name="cnabs",
    )
