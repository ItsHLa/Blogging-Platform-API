from django_filters import FilterSet
import django_filters as filter
from .models import *
from django.db import models

class BlogFilter(FilterSet):
    
    authoredBy = filter.CharFilter(method="authoredByFilter")
    
    class Meta:
        model = Blog
        fields = {
            "title" : ["contains"],
            "tags" : ["iexact"],
           
        }
    def authoredByFilter(self, queryset, name, value):
        return queryset.filter(
            models.Q(authoredBy__username__icontains = value) |
            models.Q(authoredBy__first_name__icontains = value) |
            models.Q(authoredBy__last_name__icontains = value)
        )
        
        
class CommentFilter(FilterSet):
    class Meta:
        model = Comment
        fields = {
            "blog" : ["exact"]
        }