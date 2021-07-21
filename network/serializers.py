from rest_framework import serializers
from .models import Post


class ListPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'body', 'post_date', 'total_likes')

class CreatePostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'body', 'post_date', 'total_likes')

class UpdatePostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'body', 'post_date', 'total_likes')

class DetailPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'