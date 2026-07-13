# courses/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CourseViewSet, DepartmentViewSet, EnrollmentViewSet, StudentViewSet

# Initialize automated routing generation pools
router = DefaultRouter()
router.register("departments", DepartmentViewSet)
router.register("courses", CourseViewSet)
router.register("students", StudentViewSet)
router.register("enrollments", EnrollmentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]