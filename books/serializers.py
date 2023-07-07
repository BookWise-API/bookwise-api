from rest_framework import serializers
from .models import Book
from users.serializers import NormalUserSerializer
from copies.models import Copie


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author", "description", "number_of_copies"]

    def create(self, validated_data):
        number_of_copies = validated_data.pop("number_of_copies", 0)
        book = super().create(validated_data)
        for _ in range(number_of_copies):
            Copie.objects.create(book=book)
        return book