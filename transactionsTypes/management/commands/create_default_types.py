from transactionsTypes.models import Type
from django.core.management.base import BaseCommand

data = [
    {
        "type": "1",
        "description": "Débito",
        "nature": "Entrada",
    },
    {
        "type": "2",
        "description": "Boleto",
        "nature": "Saída",
    },
    {
        "type": "3",
        "description": "Financiamento",
        "nature": "Saída",
    },
    {
        "type": "4",
        "description": "Crédito",
        "nature": "Entrada",
    },
    {
        "type": "5",
        "description": "Recebimento Empréstimo",
        "nature": "Entrada",
    },
    {
        "type": "6",
        "description": "Vendas",
        "nature": "Entrada",
    },
    {
        "type": "7",
        "description": "Recebimento TED",
        "nature": "Entrada",
    },
    {
        "type": "8",
        "description": "Recebimento DOC",
        "nature": "Entrada",
    },
    {
        "type": "9",
        "description": "Aluguel",
        "nature": "Saída",
    },
]


class Command(BaseCommand):
    help = "Create default types"

    def handle(self, *args, **kwargs):
        for i in data:
            Type.objects.create(**i)
