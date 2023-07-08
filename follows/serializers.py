from rest_framework import serializers
from .models import Follow
from rest_framework.views import Request, Response

class FollowSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Follow
        fields = [
            "id",
            "book_id",
            "user_id"
        ]
    
    def create(self, validated_data):
        return Follow.objects.create(**validated_data)