from rest_framework.viewsets import ModelViewSet

from tags.models import Tag, TaggedItem
from .serializers import TagSerializer, TaggedItemSerializer


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TaggedItemViewSet(ModelViewSet):
    queryset = TaggedItem.objects.all()
    serializer_class = TaggedItemSerializer
