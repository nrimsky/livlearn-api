from livlearn.api.models import Link, Tag
from livlearn.api.serializers import LinkSerializer, TagSerializer
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend, MultipleChoiceFilter, CharFilter, FilterSet, ModelMultipleChoiceFilter
from django_filters.fields import CSVWidget


class LinkFilter(FilterSet):

    name = CharFilter(lookup_expr='icontains')
    description = CharFilter(lookup_expr='icontains')
    tagline = CharFilter(lookup_expr='icontains')
    tags = ModelMultipleChoiceFilter(queryset=Tag.objects.all(), widget=CSVWidget())
    type = MultipleChoiceFilter(
        distinct=True, widget=CSVWidget(), choices=Link.TYPE_CHOICES
    )
    level = MultipleChoiceFilter(
        distinct=True, widget=CSVWidget(), choices=Link.LEVEL_CHOICES
    )

    class Meta:
        model = Link
        fields = ['tags', 'type', 'level', 'name', 'description', 'tagline']


class LinkListView(generics.ListAPIView):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = LinkFilter
    search_fields = ['name', 'description', 'tagline', 'tags']
    ordering_fields = ['created_at']
    ordering = ['created_at']


class TagListView(generics.ListAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering = ['name']
    ordering_fields = ['name']
    search_fields = ['name']