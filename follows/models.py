from django.db import models


class Follow(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'<Follow_id: {self.pk} | user: {self.user.username} | book: {self.book.title}>'
