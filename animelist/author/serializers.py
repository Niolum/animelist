from rest_framework import serializers
from .models import Author


class AuthorListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = ['id', 'name', 'photo']


class AuthorDetailSerializer(serializers.ModelSerializer):
    roles = serializers.SlugRelatedField(slug_field='title', read_only=True, many=True)

    class Meta:
        model = Author
        fields = '__all__'