from django.shortcuts import render
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CnabSerializer
from .forms import form
from .models import Cnab


class cnab_view(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        file = request.FILES["file"]

        for line in file:
            cnab = line.decode()
            data = {
                "type_number": cnab[0],
                "date": f"{cnab[1:5]}-{cnab[5:7]}-{cnab[7:9]}",
                "value": cnab[9:19],
                "cpf": cnab[19:30],
                "card": cnab[30:42],
                "time": f"{cnab[42:44]}:{cnab[44:46]}:{cnab[46:48]}",
                "owner": cnab[48:62],
                "store": cnab[62:],
            }
            serializer = CnabSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        data = Cnab.objects.all()
        return render(request, "results.html", {"data": data})

    def get(self, request):
        return render(request, "form.html", {"form": form})
