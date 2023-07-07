from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=150, unique=True)
    author = models.CharField(max_length=50)
    description = models.TextField()

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="books", null=True
    )
