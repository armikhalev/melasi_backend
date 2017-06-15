from rest_framework import serializers
from .models import Koyla, Card, Intro, GrammarCard


class GrammarCardSerializer(serializers.ModelSerializer):
	id = serializers.ReadOnlyField()
	class Meta:
		model = GrammarCard
		fields = ('id', 'title', 'body', 'comment')

class KoylaSerializer(serializers.ModelSerializer):
	id = serializers.ReadOnlyField()
	grammarCard = GrammarCardSerializer(read_only=True)
	class Meta:
		model = Koyla
		fields = ('id','word','la','comment','grammarCard')

class CardSerializer(serializers.ModelSerializer):
	id = serializers.ReadOnlyField()
	grammarCard = GrammarCardSerializer(read_only=True)
	class Meta:
		model = Card
		fields = ('id','front','back','flip','grammarCard')

class IntroSerializer(serializers.ModelSerializer):
	id = serializers.ReadOnlyField()
	class Meta:
		model = Intro
		fields = ('id','title','body')