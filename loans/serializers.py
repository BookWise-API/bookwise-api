from rest_framework import serializers
from .models import Loan


class LoanSerializer(serializers.ModelSerializer):
    loan_id = serializers.IntegerField(read_only=True, source="pk")
    book_id = serializers.IntegerField(read_only=True, source="copie.book.pk")

    class Meta:
        model = Loan
        fields = [
            "loan_id",
            "user_id",
            "book_id",
            "copie_id",
            "loan_date",
            "loan_return",
            "returned",
        ]
        read_only_fields = ["loan_return"]

    def create(self, validated_data):
        return Loan.objects.create(**validated_data)
