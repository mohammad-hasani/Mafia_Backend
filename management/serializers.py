from rest_framework import serializers
from . import models


class ChargePlaceHolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ChargePlaceHolder
        fields = ['id', 'charge']


class StreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Stream
        fields = ['stream']


class PlayerData(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['money', 'rank', 'score']


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Roles
        fields = ['id', 'name']