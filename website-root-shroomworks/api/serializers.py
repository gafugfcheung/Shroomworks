from django.contrib.auth.models import User
from herenow.models import Profile, Post, Location, Comment
from rest_framework import serializers
from django.db import models

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('description', 'lat', 'lon')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('caption', 'datetime', 'profile')


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    caption = serializers.CharField(required=False, allow_blank=True, max_length=100)
    time_elapsed = serializers.CharField(required=False, allow_blank=True, max_length=100)
    location = LocationSerializer(many=False, read_only=True)
    image = serializers.ImageField()

    def create(self, validated_data):
        """
        Create and return a new `Post` instance, given the validated data.
        """
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Post` instance, given the validated data.
        """
        instance.caption = validated_data.get('caption', instance.caption)
        instance.save()
        return instance
