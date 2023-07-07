from rest_framework import serializers
from .models import Follow


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
    