from rest_framework import serializers

from ..models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'slug', 'photo', 'date', 'description', 'full_text', 'full_text_mobile')
