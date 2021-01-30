from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Post
        # fields = '__all__'
        fields = [
            'pk',
            'author',
            'message',
            'created_at',
            'updated_at',
            'is_public',
            'ip',
        ]