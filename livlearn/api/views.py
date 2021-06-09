from livlearn.api.models import Test
from livlearn.api.serializers import TestSerializer
from rest_framework import viewsets


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
