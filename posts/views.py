from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from posts.serializers import PostSerializer, AuthorSerializer
from posts.models import Post, Author

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=False)
    def latest(self, request):
        latest_post = Post.objects.latest('post_date')

        serializer = self.get_serializer(latest_post, many=False)
        return Response(serializer.data)



class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @action(detail=True)
    def posts(self, request, pk=None):
        author_posts = Post.objects.filter(author__id=pk)
        serializer = PostSerializer(author_posts, many=True, context={'request': request})
        return Response(serializer.data)


