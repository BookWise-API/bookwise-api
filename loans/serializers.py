from rest_framework import serializers
from .models import Loan
from datetime import datetime, timedelta


class LoanSerializer(serializers.ModelSerializer):
    loan_id = serializers.IntegerField(read_only=True, source="pk")
    book_id = serializers.IntegerField(read_only=True, source="copy.book.pk")
    


    class Meta:
        model = Loan
        fields = [
            "loan_id",
            "user_id",
            "book_id",
            "copy_id",
            "loan_date",
            "loan_return",
            "returned",
        ]
        read_only_fields = ["loan_return"]

    # def validate_loan_return(self, attrs):
    #     current_date = datetime.now().date()
    #     return_date = current_date + timedelta(days=7)
    #     print(return_date)
    #     return return_date
    
    def create(self, validated_data):
        return Loan.objects.create(**validated_data)
