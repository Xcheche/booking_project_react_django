from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path("", views.api_root, name="api-root"),
    path("rooms/", views.RoomList.as_view(), name="room-list"),
    path("rooms/<int:pk>/", views.RoomDetail.as_view(), name="room-detail"),
    # occupied dates
    path("occupied-date", views.OccupiedDateList.as_view(), name="occupied-date"),
    path(
        "occupied-deatil/<int:pk>/",
        views.OccupiedDateDetail.as_view(),
        name="occupied-detail",
    ),
    
    # User
    path("users/", views.UserList.as_view(), name="user-list"),
    path("users/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
    #Authentication
    path("register/",views.Register.as_view(), name="register"),
    path("login/", views.Login.as_view(), name="login"),
]


urlpatterns = format_suffix_patterns(urlpatterns)
# The format_suffix_patterns function allows the API to respond to different formats like JSON or XML.
