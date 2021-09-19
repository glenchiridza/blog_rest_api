from django.shortcuts import render
from .models import BlogPost
from .serializers import (BlogPostSerializer,
                          UpdateBlogPostSerializer,
                          DeleteBlogPostSerializer)

from rest_framework import mixins
from rest_framework import generics


class PostCreateView(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


