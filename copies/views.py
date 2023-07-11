from rest_framework import generics
from rest_framework.views import Response, status, Request
from .serializers import CopieSerializer
from .models import Copie
from books.models import Book
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class CopieListView(generics.ListAPIView):
    queryset = Copie.objects.all()
    serializer_class = CopieSerializer
    
class CopieView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Copie
    serializer_class = CopieSerializer

    def create(self, request: Request, *args, **kwargs):
        serializer = CopieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        book = get_object_or_404(Book, pk=request.data["book_id"])
        serializer.save(book=book)
        return Response(serializer.data, status.HTTP_201_CREATED)