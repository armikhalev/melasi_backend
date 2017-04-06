from rest_framework import generics

from .models import Koyla
from .serializers import KoylaSerializer

class A_WordSet(generics.ListAPIView):
	queryset = Koyla.objects.filter(word__startswith='a')
	serializer_class = KoylaSerializer

	def get_queryset(self):

	    	return Koyla.objects.filter(word__startswith='a')


class D_WordSet(generics.ListAPIView):
	queryset = Koyla.objects.filter(word__startswith='d')
	serializer_class = KoylaSerializer

	def get_queryset(self):

	    	return Koyla.objects.filter(word__startswith='d')


class F_WordSet(generics.ListAPIView):
	queryset = Koyla.objects.filter(word__startswith='f')
	serializer_class = KoylaSerializer

	def get_queryset(self):

	    	return Koyla.objects.filter(word__startswith='f')

####################### Here starts the Mela dictionary ######################

class A_LaSet(generics.ListAPIView):
	queryset = Koyla.objects.filter(la__startswith='a')
	serializer_class = KoylaSerializer

	def get_queryset(self):

	    	return Koyla.objects.filter(la__startswith='a')


class D_LaSet(generics.ListAPIView):
	queryset = Koyla.objects.filter(la__startswith='d')
	serializer_class = KoylaSerializer

	def get_queryset(self):

	    	return Koyla.objects.filter(la__startswith='d')


class F_LaSet(generics.ListAPIView):
	queryset = Koyla.objects.filter(la__startswith='f')
	serializer_class = KoylaSerializer

	def get_queryset(self):

	    	return Koyla.objects.filter(la__startswith='f')
