from rest_framework import serializers

from feed.models import FeedModel


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedModel
        fields = '__all__'