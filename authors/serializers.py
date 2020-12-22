from rest_framework import serializers
from authors.models import Authors

# class AuthorsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model: Authors
#         fields: ['id', 'name', 'nationality']

class AuthorsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    nationality = serializers.CharField(required=True, max_length=50)

    def create(self, validated_data):
        return Authors.objects.create(**validated_data)