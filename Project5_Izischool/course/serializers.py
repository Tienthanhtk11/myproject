from rest_framework import serializers

from course.models import course


class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, max_length=256)
    subtitle = serializers.CharField(required=False, max_length=256)
    image = serializers.CharField(required=False, max_length=256)
    price = serializers.FloatField(required=False)
    hitcount = serializers.IntegerField(required=False)

    def create(self, validated_data):
        return course.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.subtitle = validated_data.get('subtitle', instance.subtitle)
        instance.image = validated_data.get('image', instance.image)
        instance.price = validated_data.get('price', instance.price)
        instance.hitcount = validated_data.get('hitcount', instance.hitcount)
        instance.save()
        return instance

