from rest_framework import generics
from rest_framework.views import Response, status, Request
from .serializers import CopieSerializer
from .models import Copie
from books.models import Book
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_spectacular.utils import extend_schema


class CopieListView(generics.ListAPIView):
    queryset = Copie.objects.all()
    serializer_class = CopieSerializer

    @extend_schema(
        operation_id="get_copie",
        description="Rota de listagem de cópias. Aceita parâmetro opcional de paginação ex: .../api/copies/?page=2/. Não requer autenticação.",
        summary="Listar todas as cópias",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
