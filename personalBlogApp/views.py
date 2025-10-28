from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import *
from .models import *
from .filter import *

# Create your views here.

class MyBlogsView(viewsets.ModelViewSet):
    serializer_class = BlogDetailSerializer
    
    def get_queryset(self):
        return self.request.user.authoredBlogs.all()

class BlogsView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = BlogFilter
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return BlogSerializer
        return BlogDetailSerializer
        
class CommentsView(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer
    
    def get_serializer_context(self):
        return {"blog" : self.kwargs['blog_pk']}
    
    def get_queryset(self):
        blog = self.kwargs["blog_pk"]
        if blog:
            return Comment.objects.filter(blog_id = blog)
        return super().get_queryset()
    
    def perform_create(self, serializer):
        author = self.request.user.id
        blog = self.kwargs['blog_pk']
        return serializer.save(
            authorBy_id = author,
            blog_id = blog)
         
