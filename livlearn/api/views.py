from livlearn.api.models import Link, Tag
from livlearn.api.serializers import LinkSerializer, TagSerializer
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class LinkListView(generics.ListAPIView):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description', 'tagline', 'tags']
    ordering_fields = ['created_at']
    filterset_fields = '__all__'
    ordering = ['created_at']


class TagListView(generics.ListAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering = ['name']
    ordering_fields = ['name']
    search_fields = ['name']