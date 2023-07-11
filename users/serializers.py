from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from follows.serializers import FollowSerializer
from loans.serializers import LoanSerializer
from .models import User


class NormalUserSerializer(serializers.ModelSerializer):
    followed_books = FollowSerializer(many=True, read_only=True)
    borrowed_books = LoanSerializer(many=True, read_only=True)

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        password = validated_data.pop("password", None)
        if password:
            instance.set_password(password)
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "name",
            "blocked_until",
            "is_admin",
            "followed_books",
            "borrowed_books",
        ]
        read_only_fields = [
            "id",
            "is_admin",
            "blocked_until",
            "followed_books",
            "borrowed_books",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="This username already exists.",
                    )
                ]
            },
            "email": {"validators": [UniqueValidator(queryset=User.objects.all())]},
        }


class AdminManageUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        password = validated_data.pop("password", None)
        if password:
            instance.set_password(password)
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "name",
            "blocked_until",
            "is_admin",
        ]
        read_only_fields = ["id"]
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="This username already exists.",
                    )
                ]
            },
            "email": {"validators": [UniqueValidator(queryset=User.objects.all())]},
        }
