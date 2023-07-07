from rest_framework import generics
from copies.models import Copie
from copies.serializer import CopieSerializer


class CopieListView(generics.ListAPIView):
    queryset = Copie.objects.all()
    serializer_class = CopieSerializer