from datetime import datetime

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from ..models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostApiView(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(date__lte=datetime.today())
