from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.views import APIView    
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed,PermissionDenied
from rest_framework.authtoken.models import Token

# Create your views here.
# Genreic Api views for listing, creating, retrieving, updating, and deleting rooms
# This file contains the views for the booking API, including the API root view and views for listing, creating, retrieving, updating, and deleting rooms.
# The views use Django REST Framework's generic views to handle common operations on the Room model.
# This file contains the views for the booking API, including the API root view and views for listing, creating, retrieving, updating, and deleting rooms.
@api_view(["GET"])
def api_root(request, format=None):
    """
    API root view that provides links to the available endpoints.
    """
    return Response(
        {
            "rooms": reverse("room-list", request=request, format=format),
        }
    )


class RoomList(
    generics.ListCreateAPIView
):  # ListCreateAPIView allows listing and creating rooms
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomDetail(
    generics.RetrieveUpdateDestroyAPIView
):  # RetrieveUpdateDestroyAPIView allows retrieving, updating, and deleting a room
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


# Ocupied date
class OccupiedDateList(
    generics.ListCreateAPIView
):  # ListCreateAPIView allows listing and creating rooms
    queryset = OccupiedDate.objects.all()
    serializer_class = OccupiedDateSerializer

    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser and not user.is_staf:  #if not staff or admin they can only see their own stuff
            return OccupiedDate.objects.filter(user=user)
        return super().get_queryset()


class OccupiedDateDetail(
    generics.RetrieveUpdateDestroyAPIView
):  # RetrieveUpdateDestroyAPIView allows retrieving, updating, and deleting a room
    queryset = OccupiedDate.objects.all()
    serializer_class = RoomSerializer






#User


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:  # Admin or staff users can see all users
            return User.objects.all()
        else:  # Regular users
            return User.objects.filter(id=user.id)
    

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        user = self.request.user
        obj = super().get_object()

        # Allow access if the user is fetching their own details or is an admin
        if obj == user or user.is_staff or user.is_superuser:
            return obj
        else:
            raise permissions.PermissionDenied("You do not have permission to access this user's details.")
        
        
#Register
    
class Register(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        # Save the user
        user = serializer.save()

        # Generate token
        token, created = Token.objects.get_or_create(user=user)

        # Return user data and token in response
        self.response_data = {
            "user": {
                "id": user.id,
                "username": user.email,
                "email": user.email,
                "full_name":user.full_name
            },
            "token": token.key,
        }

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response(self.response_data)
    
        
    
class Login(APIView):
    def post(self, request, *args, **kwargs):
        # Extract username and password from the request data
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user is None:
            # Raise an error if authentication fails
            raise AuthenticationFailed('Invalid username or password')

        # Generate or retrieve the token
        token, created = Token.objects.get_or_create(user=user)

        # Return the user info and token
        return Response({
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "full_name":user.full_name
            },
            "token": token.key,
        })
    
    