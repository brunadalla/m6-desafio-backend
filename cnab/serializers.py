from rest_framework import serializers
from .models import Cnab
from transactionsTypes.models import Type


class CnabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cnab
        fields = "__all__"
        read_only_fields = ["id",]

    def create(self, validated_data):
        type = validated_data.pop("type")
        created_type, _ = Type.objects.get_or_create(**type)

        return Cnab.objects.create(**validated_data, type=created_type)
