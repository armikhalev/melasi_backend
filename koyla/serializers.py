from rest_framework import serializers
from .models import Koyla, Card

class KoylaSerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.ReadOnlyField()
	class Meta:
		model = Koyla
		fields = ('id','word','la','comment')

class CardSerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.ReadOnlyField()
	class Meta:
		model = Card
		fields = ('id','front','back','flip')
