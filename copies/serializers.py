from rest_framework import serializers
from .models import Copie


class CopieSerializer(serializers.ModelSerializer):
    book_id = serializers.IntegerField(source="book.pk")

    class Meta:
        model = Copie
        fields = [
            "id",
            "book_id",
            "is_borrowed"
        ]
        read_only_fields = ["id", "is_borrowed"]
