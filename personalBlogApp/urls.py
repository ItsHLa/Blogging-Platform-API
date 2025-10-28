from django.urls import path, include
from rest_framework_nested import routers
from .views import *

router = routers.DefaultRouter()
router.register('blogs', BlogsView)
router.register('myblogs', MyBlogsView, basename='myblog')

blog_router = routers.NestedDefaultRouter(router,'blogs', lookup = 'blog')
blog_router.register("comments", CommentsView, basename='blog-comment')

my_blog_router = routers.NestedDefaultRouter(router, 'myblogs', lookup = 'blog')
my_blog_router.register("comments", CommentsView, basename='myblog-comment')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(blog_router.urls)),
    path('', include(my_blog_router.urls))
]