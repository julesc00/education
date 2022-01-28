from abc import ABC

from rest_framework import serializers

from courses.models import Course, Subject, Module, Content


class ItemRelatedField(serializers.RelatedField, ABC):
    def to_representation(self, value):
        return value.render()


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ["id", "title", "slug"]
        read_only_fields = ("id",)


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ["order", "title", "description"]


class CourseSerializer(serializers.ModelSerializer):

    # Nested serializer
    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ["id", "subject", "title", "slug", "overview", "created", "owner", "modules"]
        read_only_fields = ("id",)


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ["order", "item"]
        read_only_fields = ("id",)


class ModuleWithContentSerializer(serializers.ModelSerializer):
    contents = ContentSerializer

    class Meta:
        model = Module
        fields = ["order", "title", "description", "contents"]
        read_only_fields = ("id",)


class CourseWithContentSerializer(serializers.ModelSerializer):
    modules = ModuleWithContentSerializer(many=True)

    class Meta:
        model = Course
        fields = ["id", "subject", "title", "slug", "overview", "created", "owner", "modules"]
