from django.shortcuts import render
from rest_framework import generics
from .models import Room
from .serializers import RoomSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse
# Create your views here.
#Genreic Api views for listing, creating, retrieving, updating, and deleting rooms
# This file contains the views for the booking API, including the API root view and views for listing, creating, retrieving, updating, and deleting rooms.
# The views use Django REST Framework's generic views to handle common operations on the Room model.
# This file contains the views for the booking API, including the API root view and views for listing, creating, retrieving, updating, and deleting rooms.
@api_view(['GET'])
def api_root(request, format=None):
    """
    API root view that provides links to the available endpoints.
    """
    return Response({
        'rooms': reverse('room-list', request=request, format=format),      
    })

class RoomList(generics.ListCreateAPIView): # ListCreateAPIView allows listing and creating rooms
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
    
class RoomDetail(generics.RetrieveUpdateDestroyAPIView): # RetrieveUpdateDestroyAPIView allows retrieving, updating, and deleting a room  
      queryset = Room.objects.all()
      serializer_class = RoomSerializer
     