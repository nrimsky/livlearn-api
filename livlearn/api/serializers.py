from rest_framework import serializers
from livlearn.api.models import Test


class TestSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Test
        fields = '__all__'
