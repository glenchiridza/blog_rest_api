from rest_framework import serializers
from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author_name.username", read_only=True)

    class Meta:
        model = BlogPost
        fields = ('id', 'author_name', 'author',
                  'featured_image', 'title', 'subtitle', 'content'
                  , 'post_date')


class UpdateBlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('__all__',)


class DeleteBlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('__all__',)
