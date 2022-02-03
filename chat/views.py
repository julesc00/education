from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404


@login_required
def course_chat_room_view(request, course_id):
    try:
        # Retrieve course with given id joined by the current user
        course = request.user.courses_joined.get(id=course_id)
    except ConnectionRefusedError:
        # user is not a student of the course or course does not exist
        return HttpResponseForbidden()

    context = {"course": course}
    return render(request, "chat/room.html", context)
