from rest_framework import serializers
from .models import Copy


class CopySerializer(serializers.ModelSerializer):
    book_id = serializers.IntegerField(source="book.pk")

    class Meta:
        model = Copy
        fields = [
            "id",
            "book_id",
            "is_borrowed"
        ]
        read_only_fields = ["id", "is_borrowed"]
