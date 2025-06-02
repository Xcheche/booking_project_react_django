from rest_framework import serializers
from .models import *

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        # fields = '__all__'
        fields = ['url','id', 'name', 'room_type', 'price_per_night', 'currency', 'max_occupancy', 'description']        