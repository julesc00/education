from django.urls import path

from .views import ManageCourseListView, CourseCreateView, CourseUpdateView, CourseDeleteView

app_name = "courses"

urlpatterns = [
    path("mine/", ManageCourseListView.as_view(), name="manage_course_list"),
    path("create/", CourseCreateView.as_view(), name="course_create"),
    path("<int:pk>/edit/", CourseUpdateView.as_view(), name="course_edit"),
    path("<int:pk>/delete/", CourseDeleteView.as_view(), name="course_delete"),
]
