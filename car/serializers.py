from turtle import title
from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    is_publisher = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)

    
    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.is_publisher = validated_data.get("is_publisher", instance.is_publisher)
        instance.cat_id = validated_data.get("cat_id", instance.cat_id)
        instance.save()
        return instance

# class CarSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Car
#         fields = "__all__"