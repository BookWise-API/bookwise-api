from django.db import models

class Copie(models.Model):
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    is_borrowed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"<Copy_id: {self.pk} | book: {self.book.title}>"
