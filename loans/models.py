from django.db import models


class Loan(models.Model):
    loan_date = models.DateField(auto_now=True)
    loan_return = models.DateField()
    returned = models.DateField(default=None, null=True)
    copy = models.ForeignKey('copies.Copy', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"<Loan_id: {self.pk} | book: {self.copy.book.title} | user: {self.user.username}>"
