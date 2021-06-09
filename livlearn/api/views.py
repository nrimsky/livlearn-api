from livlearn.api.models import Link, Tag
from livlearn.api.serializers import LinkSerializer, TagSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


class LinkListView(generics.ListCreateAPIView):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'


class TagListView(generics.ListCreateAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()