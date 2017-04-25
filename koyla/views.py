from rest_framework import generics

from .models import Koyla
from .serializers import KoylaSerializer

# English words
class WordSet(generics.ListAPIView):

	serializer_class = KoylaSerializer

	def get_queryset(self):
		queryset = self.kwargs['letter']
		return Koyla.objects.filter(word__startswith=queryset)

# Mela words
class LaSet(generics.ListAPIView):

	serializer_class = KoylaSerializer

	def get_queryset(self):
		queryset = self.kwargs['letter']
		return Koyla.objects.filter(la__startswith=queryset)
