from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAdminUser
from rest_framework import generics
from books.models import Book
from books.serializers import BookSerializer
from drf_spectacular.utils import extend_schema


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @extend_schema(
        operation_id="get_book",
        description="Rota para listagem de livros",
        summary="Listar livros",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class BookCreateView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @extend_schema(
        operation_id="post_book",
        description="Rota para criação de livro",
        summary="Criar livro",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class BookDetailsView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @extend_schema(
        operation_id="get_id_book",
        description="Rota de listagem de livro",
        summary="Listar livro",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(operation_id="put_id_book", exclude=True)
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        operation_id="patch_id_book",
        description="Rota de atualização de livro",
        summary="Atualizar livro",
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        operation_id="delete_id_book",
        description="Rota de deleção de livro",
        summary="Deletar livro",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
