from rest_framework import serializers
from .models import Book
from users.serializers import NormalUserSerializer


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author", "description"]
