from rest_framework import serializers
from .models import Anime, Manga, Ranobe
from author.serializers import AuthorListSerializer
from character.serializers import CharacterListSerializer
from comment.serializers import CommentSerializer


class AnimeListSerializer(serializers.ModelSerializer):
    rating_user = serializers.BooleanField()
    middle_star = serializers.IntegerField()

    class Meta:
        model = Anime
        fields = ['id', 'title', 'types', 'rating_user', 'middle_star']


class AnimeDetailSerializer(serializers.ModelSerializer):

    authors = AuthorListSerializer(read_only=True, many=True)
    characters = CharacterListSerializer(read_only=True, many=True)
    genres = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    studios = serializers.SlugRelatedField(slug_field="title", read_only=True, many=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Anime
        exclude = ("draft", )


class MangaListSerializer(serializers.ModelSerializer):
    rating_user = serializers.BooleanField()
    middle_star = serializers.IntegerField()

    class Meta:
        model = Manga
        fields = ['id', 'title', 'types', 'rating_user', 'middle_star']


class MangaDetailSerializer(serializers.ModelSerializer):

    authors = AuthorListSerializer(read_only=True, many=True)
    characters = CharacterListSerializer(read_only=True, many=True)
    genres = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    publisher = serializers.SlugRelatedField(slug_field="title", read_only=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Manga
        exclude = ("draft", )


class RanobeListSerializer(serializers.ModelSerializer):
    rating_user = serializers.BooleanField()
    middle_star = serializers.IntegerField()

    class Meta:
        model = Ranobe
        fields = ['id', 'title', 'types', 'rating_user', 'middle_star']


class RanobeDetailSerializer(serializers.ModelSerializer):

    authors = AuthorListSerializer(read_only=True, many=True)
    characters = CharacterListSerializer(read_only=True, many=True)
    genres = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    publisher = serializers.SlugRelatedField(slug_field="title", read_only=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Ranobe
        exclude = ("draft", )