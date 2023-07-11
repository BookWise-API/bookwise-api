from django.db import models


class Follow(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="followed_books")
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'PK: {self.pk} / user: {self.user} / book: {self.book}'
