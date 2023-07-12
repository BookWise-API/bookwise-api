from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Follow
from copies.models import Copie
from .serializers import FollowSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import Request, Response, status
from books.models import Book
from drf_spectacular.utils import extend_schema
from django.core.mail import send_mail
from django.conf import settings


class FollowView(generics.UpdateAPIView):
    """
    Seguir um livro
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Book.objects.all()
    serializer_class = FollowSerializer

    def update(self, request, **kwargs):
        book_found = self.get_object()

        try:
            follow_found = Follow.objects.get(book=book_found, user=request.user)
            follow_found.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Follow.DoesNotExist:
            serializer = FollowSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user, book=book_found)

            """
            Email informativo da disponibilidade/status do livro
            """
            avaliable_copies = Copie.objects.filter(book=book_found, is_borrowed=False)

            if len(avaliable_copies) > 0:
                send_mail(
                subject="Bookwise - Disponibilidade do livro seguido",
                message=f"Informamos que temos {len(avaliable_copies)} cópias do livro {book_found.title} a sua disposição. A equipe Bookwise agradece a preferência!",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[request.user.email],
                fail_silently=False
            )
                
            else:
                send_mail(
                subject="Bookwise - Indisponibilidade do livro seguido",
                message=f"Informamos que o livro {book_found.title} se encontra indisponível no momento. Mas não se preocupe: logo teremos um exemplar disponível! Atenciosamente a equipe Bookwise.",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[request.user.email],
                fail_silently=False
            )
            
            return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        operation_id="put_follows",
        description="Rota para seguir um livro. Usuário precisa estar logado.",
        summary="Seguir um livro",
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(operation_id="patch_follows", exclude=True)
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
