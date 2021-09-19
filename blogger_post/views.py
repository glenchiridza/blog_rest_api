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


class GetSinglePostView(mixins.ListModelMixin, generics.RetrieveAPIView):
    serializer_class = BlogPostSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)

    def get_queryset(self):
        queryset = BlogPost.objects.filter(id=self.kwargs['pk'])
        return queryset


class PostUpdateView(generics.UpdateAPIView):
    serializer_class = UpdateBlogPostSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = BlogPost.objects.filter(id=self.kwargs['pk'])
        return queryset


class PostDeleteView(generics.DestroyAPIView):
    serializer_class = DeleteBlogPostSerializer
    queryset = BlogPost.objects.all()
    lookup_field = 'pk'
