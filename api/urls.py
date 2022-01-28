from django.urls import path, include

from rest_framework import routers

from .views import SubjectListView, SubjectDetailView, CourseViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register("courses", CourseViewSet)

urlpatterns = [
    path("subjects/", SubjectListView.as_view(), name="subject_list"),
    path("subjects/<int:pk>/", SubjectDetailView.as_view(), name="subject_detail"),

    path("", include(router.urls)),
]
