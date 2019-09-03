from qanda.models import User, Tag, Post, Image
from rest_framework import serializers


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['url', 'id', 'genre']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'user_id', 'created', 'information', 'familiar_tag', 'studying_tag',
                  'header_image', 'profile_image', 'following']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['url', 'id', 'owner', 'created', 'header', 'body', 'tag', 'posts_to']


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['url', 'id', 'post', 'image']
