from .models import Singer, Song
from rest_framework import serializers

class SingerSerializer(serializers.ModelSerializer):
	# songs = serializers.StringRelatedField(many=True, read_only=True)
	# songs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	# songs = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail')
	# songs = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
	songs = serializers.HyperlinkedIdentityField(view_name='song-detail', many=True, read_only=True)
	class Meta:
		model = Singer
		fields = ['id', 'name', 'gender', 'songs']

class SongSerializer(serializers.ModelSerializer):
	class Meta:
		model = Song
		fields = '__all__'