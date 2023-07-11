from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Follow
from .serializers import FollowSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import Request, Response, status
from django.shortcuts import get_object_or_404
from books.models import Book
from drf_spectacular.utils import extend_schema


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
            return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        operation_id="put_follows",
        description="Rota para seguir um livro",
        summary="Seguir um livro",
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(operation_id="patch_follows", exclude=True)
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
