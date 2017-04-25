from rest_framework import generics

from .models import Koyla
from .serializers import KoylaSerializer

# English words
class WordSet(generics.ListAPIView):

	serializer_class = KoylaSerializer
     
	def get_queryset(self):
		queryset = Koyla.objects.all()
		letter = self.request.query_params.get('letter', None)
		if letter is not None:
			queryset = queryset.filter(word__startswith=letter)

		return queryset

# Mela words
class LaSet(generics.ListAPIView):

	serializer_class = KoylaSerializer
     
	def get_queryset(self):
		queryset = Koyla.objects.all()
		la = self.request.query_params.get('la', None)
		if la is not None:
			queryset = queryset.filter(la__startswith=la)

		return queryset