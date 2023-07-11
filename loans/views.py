from rest_framework import generics
from rest_framework.views import Response, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Loan
from .serializers import LoanSerializer
from copies.models import Copie
from datetime import datetime, timedelta


class LoanView(generics.UpdateAPIView):
    """
    Emprestar uma cópia de um livro
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Copie.objects.all()
    serializer_class = LoanSerializer

    def update(self, request, **kwargs):
        current_date = datetime.now().date()
        devolution_date = current_date + timedelta(days=7)
        Copie_found = self.get_object()
        user = request.user

        if user.blocked_until is not None:
            verify_block = current_date - user.blocked_until.date()

            if verify_block.days < 0:
                """
                Verifica se o usuário está com empréstimos bloqueados
                """
                return Response({"detail": "Blocked user, loan not accepted"})

        try:
            """
            Procura emprestimo com mesmo user e Copie, em aberto
            """
            loan_found = Loan.objects.get(
                Copie=Copie_found, user=request.user, returned=None)

        except Loan.DoesNotExist:
            """
            Primeiro emprestimo com o mesmo user e Copie,
            ou não há este empréstimo em aberto, criando-se um novo.
            """
            serializer = LoanSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(loan_return=devolution_date,
                            Copie=Copie_found, user=request.user)
            return Response(serializer.data, status.HTTP_200_OK)

        loan_found.returned = current_date
        loan_found.save()
        serializer = LoanSerializer(instance=loan_found)
        late_return = (loan_found.loan_return - loan_found.returned).days

        if late_return < 0:
            """
            Ativa o bloqueio para empréstimo ao usuário
            """
            block_until = current_date + timedelta(days=5)
            user.blocked_until = block_until
            user.save()

        return Response(serializer.data, status.HTTP_200_OK)
