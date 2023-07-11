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
