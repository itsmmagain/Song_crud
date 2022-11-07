from rest_framework import serializers
from .models import Song, Artiste

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ["id", "First_name", "Last_name"]

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["id", "Title", "Release_date"]
