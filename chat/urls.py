from django.urls import path

from .views import course_chat_room_view

app_name = "chat"

urlpatterns = [
    path("room/<int:course_id>/", course_chat_room_view, name="course_chat_room"),
]
