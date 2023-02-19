from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from ..models import Room, Category
from .serializers import RoomSerializer, CategorySerializer


class RoomApiView(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_field = 'slug'


class CategoryApiView(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
