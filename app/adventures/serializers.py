from rest_framework import serializers

from app.adventures.models import User, Adventure, Event


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "hashed_password"]


class AdventureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Adventure
        fields = [
            "url",
            "user_id",
            "name",
            "description",
            "start_level",
            "estimated_end_level",
            "estimated_duration",
        ]
        
        
class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = [
            "url",
            "adventure_id",
            "name",
            "description",
            "expected_level",
        ]
