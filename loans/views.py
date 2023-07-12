from rest_framework import generics
from rest_framework.views import Response, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Loan
from .serializers import LoanSerializer
from copies.models import Copie
from datetime import datetime, timedelta
from drf_spectacular.utils import extend_schema
from django.core.mail import send_mail
from django.conf import settings


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
        copie_found = self.get_object()
        user = request.user

        try:
            """
            Procura emprestimo com mesmo user e Copie, em aberto
            """
            loan_found = Loan.objects.get(
                copie=copie_found, user=request.user, returned=None
            )

        except Loan.DoesNotExist:
            """
            Primeiro emprestimo com o mesmo user e Copie,
            ou não há este empréstimo em aberto, criando-se um novo.
            """
            if user.blocked_until is not None:
                verify_block = current_date - user.blocked_until.date()

                if verify_block.days < 0:
                    """
                    Verifica se o usuário está com empréstimos bloqueados
                    """
                    return Response({"detail": "Blocked user, loan not accepted"})
                
            if copie_found.is_borrowed:
                """
                Verifica se a copia está disponível 
                """
                return Response({"detail": "Sorry, This copie is already borrowed"})            

            serializer = LoanSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(
                loan_return=devolution_date, copie=copie_found, user=request.user
            )
            copie_found.is_borrowed = True
            copie_found.save()
            """
            Email informativo de empréstimo
            """
            send_mail(
                subject="Bookwise - Empréstimo de livro",
                message=f"Empréstimo do livro {copie_found.book.title} em sua conta realizado com sucesso! Favor devolver este livro até o dia {devolution_date.strftime('%d/%m/%Y')} para evitar bloqueio da conta. A equipe Bookwise agradece a preferência!",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=False
            )
            return Response(serializer.data, status.HTTP_200_OK)
        
        copie_found.is_borrowed = False
        copie_found.save()
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
            """
            Email informativo de bloqueio de conta
            """
            send_mail(
                subject="Bookwise - Bloqueio de conta",
                message=f"Informamos que sua conta está bloqueada por motivo de atraso na devolução do livro {copie_found.book.title}. Você poderá voltar a emprestar normalmente a partir do dia {block_until.strftime('%d/%m/%Y')}. Atenciosamente, a equipe Bookwise.",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=False
            )

        """
        Email informativo de devolução
        """
        send_mail(
                subject="Bookwise - Devolução de livro",
                message=f"Confirmada a devolução do livro {copie_found.book.title} em {current_date.strftime('%d/%m/%Y')}! A equipe Bookwise agradece a preferência!",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=False
            )

        return Response(serializer.data, status.HTTP_200_OK)

    @extend_schema(
        operation_id="put_loans",
        description="Rota para fazer empréstimo ou devolução de um livro. Usuário precisa estar logado.",
        summary="Alugar ou devolver um livro",
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(operation_id="patch_loans", exclude=True)
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
