from django.contrib.auth.models import User
from herenow.models import Profile, Post, Location, Comment, Like
from rest_framework import serializers
from django.db import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        """ Gets the user basic information """
        model = User
        fields = ('id', 'username', 'email')


class UserThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        """ Gets the user first name for the posts list serializer """
        model = User
        fields = ('first_name')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        """ Gets the location to use in the posts view """
        model = Location
        fields = ('description', 'lat', 'lon')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        """ Gets comments to use in post api """
        model = Comment
        fields = ('caption', 'datetime')


class ProfileThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        """ Gets profile thumbnail to use in posts list view """
        model = Profile
        fields = ('image', )


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        """ Gets likes for posts details view """
        model = Like
        fields = ('profile', )


class PostSerializer(serializers.Serializer):
    """ Shows complete post information to use in fullscreen view """
    id = serializers.IntegerField(read_only=True)
    caption = serializers.CharField(required=False, allow_blank=True, max_length=100)
    time_elapsed = serializers.CharField(required=False, allow_blank=True, max_length=100)
    location = LocationSerializer(many=False, read_only=True)
    profile = ProfileThumbnailSerializer(many=False, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)
    user = UserSerializer(many=False, read_only=True)
    comments_count = serializers.IntegerField(source='comment_post.count')
    like_count = serializers.IntegerField(source='like_post.count')
    image = serializers.ImageField()


class PostPreviewSerializer(serializers.Serializer):
    """ Gets basic post information to be used in the map and list view """
    id = serializers.IntegerField(read_only=True)
    caption = serializers.CharField(required=False, allow_blank=True, max_length=100)
    time_elapsed = serializers.CharField(required=False, allow_blank=True, max_length=100)
    location = LocationSerializer(many=False, read_only=True)
    profile = ProfileThumbnailSerializer(many=False, read_only=True)
    user = UserSerializer(many=False, read_only=True)
    comments_count = serializers.IntegerField(source='comment_post.count')
    like_count = serializers.IntegerField(source='like_post.count')
    image = serializers.ImageField()
