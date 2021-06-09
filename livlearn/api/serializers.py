from rest_framework import serializers
from livlearn.api.models import Tag, Link


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class LinkSerializer(serializers.ModelSerializer):

    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Link
        fields = '__all__'
