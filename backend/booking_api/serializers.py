from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password


class RoomImageSerializer(serializers.ModelSerializer):
    room = serializers.HyperlinkedRelatedField(
        view_name="room-detail",  # Assuming you have a view named 'room-detail'
        queryset=Room.objects.all(),  # To match the related_name in RoomImage model
    )

    class Meta:
        model = RoomImage
        fields = ["id", "image", "caption", "room"]


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    images = RoomImageSerializer(
        many=True, read_only=True
    )  # To match related_name in RoomImage model

    class Meta:
        model = Room
        # fields = '__all__'
        fields = [
            "url",
            "id",
            "name",
            "room_type",
            "price_per_night",
            "currency",
            "max_occupancy",
            "description",
            "images",  # to match related_name in RoomImage model
        ]


class OccupiedDateSerializer(serializers.ModelSerializer):
    room = serializers.HyperlinkedRelatedField(
        view_name="room-detail",  # Assuming you have a view named 'room-detail'
        queryset=Room.objects.all(),  # To match the related_name in OccupiedDates model
    )

    class Meta:
        model = OccupiedDate
        fields = ["url", "id", "room", "date"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =User
        fields = ['url','username','password','email','first_name']
    def validate_password(self, value):
        """
        Hash the password before saving it.
        """
        return make_password(value)    
    