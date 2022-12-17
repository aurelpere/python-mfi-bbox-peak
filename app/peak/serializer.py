from rest_framework import serializers
from peak.models import Peak


# Create your models here.
class PeakSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Peak
        fields = ('id', 'name', 'altitude', 'latitude', 'longitude', 'point')
