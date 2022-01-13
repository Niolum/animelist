from rest_framework import serializers
from .models import Rating


class CreateRatingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Rating
        fields = ['star', 'general']

    def create(self, validated_data):
        rating, _ = Rating.objects.update_or_create(
            ip=validated_data.get('ip', None),
            general=validated_data.get('general', None),
            defaults={'star':validated_data.get('star')}
        )
        return rating