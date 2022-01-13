from rest_framework import serializers
from .models import Character
from author.serializers import AuthorListSerializer


class CharacterListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Character
        fields = ['id', 'name', 'photo']


class CharacterDetailSerializer(serializers.ModelSerializer):
    seiyu = AuthorListSerializer(read_only=True, many=True)

    class Meta:
        model = Character
        fields = '__all__'
