from rest_framework import generics

from .models import Koyla, Card, Intro, GrammarCard
from .serializers import KoylaSerializer, CardSerializer, IntroSerializer, GrammarCardSerializer

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
		la = self.request.query_params.get('letter', None)
		if la is not None:
			queryset = queryset.filter(la__startswith=la)

		return queryset

# Cards for building blocks view
class CardSet(generics.ListAPIView):

	serializer_class = CardSerializer

	def get_queryset(self):
		queryset = Card.objects.all()
		return queryset

class IntroSet(generics.ListAPIView):
	serializer_class = IntroSerializer

	def get_queryset(self):
		queryset = Intro.objects.all()
		return queryset

class GrammarCardSet(generics.ListAPIView):
	serializer_class = GrammarCardSerializer

	def get_queryset(self):
		queryset = GrammarCard.objects.all()
		id = self.request.query_params.get('id', None)
		if id is not None:
			queryset = queryset.filter(id=id)
		return queryset
