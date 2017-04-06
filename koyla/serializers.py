from rest_framework import serializers
from .models import Koyla

class KoylaSerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.ReadOnlyField()
	class Meta:
		model = Koyla
		fields = ('id','word','la','comment')
