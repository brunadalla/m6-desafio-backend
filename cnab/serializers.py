from rest_framework import serializers
from .models import Cnab
from transactionsTypes.models import Type


class CnabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cnab
        fields = "__all__"
        read_only_fields = [
            "id",
            "type",
        ]
        extra_kwargs = {"type_number": {"write_only": True}}

    def create(self, validated_data):
        type = Type.objects.get(type=validated_data["type_number"])

        return Cnab.objects.create(**validated_data, type=type)
