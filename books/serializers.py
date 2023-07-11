from rest_framework import serializers
from .models import Book
from copies.serializers import CopieSerializer
from copies.models import Copie


class BookSerializer(serializers.ModelSerializer):
    copies = CopieSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ["id", "title", "author", "description", "number_of_copies", "copies"]
        read_only_fields = ["id", "copies"]

    def create(self, validated_data):
        number_of_copies = validated_data.get("number_of_copies", 0)
        print(number_of_copies)
        book = super().create(validated_data)
        for _ in range(number_of_copies):
            Copie.objects.create(book=book)
        return book
