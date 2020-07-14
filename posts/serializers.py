from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Post, Author

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'post_date', 'url']

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'email', 'url']