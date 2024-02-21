from rest_framework import serializers
from django.contrib.auth.models import User
from cource import models


class CourseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lesson
        fields = ("title", "video_url", "total_time")


class CourseSerializer(serializers.ModelSerializer):
    is_buy = serializers.BooleanField()
    user = CourseUserSerializer()
    lesson = LessonSerializer()

    class Meta:
        model = models.LessonUser
        fields = ("title", "user", "lesson", "is_buy", "status", "watched", "total")
