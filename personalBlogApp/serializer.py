from rest_framework import serializers

from .models import *

class BlogCountMixin:
    comments_count = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    
    def get_comments_count(self, obj):
        print(f"Debug: Blog ID {obj.id}, Comments count: {obj.BlogComments.count()}")
        return obj.BlogComments.count()
    
    def get_likes_count(self, obj):
        print(f"Debug: Blog ID {obj.id}, Likes count: {obj.BlogComments.count()}")
        return obj.likedBy.count()
    
class BlogSerializer(BlogCountMixin, serializers.ModelSerializer):  
    authoredBy = serializers.ReadOnlyField(source = "authoredBy.username")
    comments_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()
    
    class Meta:
        model = Blog
        fields = ["id","title", "tags", "authoredBy", "createdAt",  "likes_count","comments_count" ]
    
class BlogDetailSerializer(BlogCountMixin, serializers.ModelSerializer):
    comments_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()
    
    
    class Meta:
        model = Blog
        fields = "__all__"
       
class CommentsSerializer(serializers.ModelSerializer):
    authorBy = serializers.ReadOnlyField(source = 'authorBy.username')
    
    class Meta:
        model = Comment
        fields = '__all__'