from rest_framework import serializers
from .models import Type


class TypeSerializer(serializers.ModelSerializer):
    signal = serializers.SerializerMethodField()

    class Meta:
        model = Type
        fields = ["id", "type", "description", "nature", "signal"]
        read_only_fields = ["id", "signal"]

    def get_signal(self, obj):
        if obj.nature == "In":
            return "+"
        return "-"

    def create(self, validated_data):
        return Type.objects.create(**validated_data)
