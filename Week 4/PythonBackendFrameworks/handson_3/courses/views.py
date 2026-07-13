# courses/views.py
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Course, Department, Enrollment, Student
from .serializers import (
    CourseSerializer,
    DepartmentSerializer,
    EnrollmentSerializer,
    StudentSerializer,
)


class CourseViewSet(viewsets.ModelViewSet):
    """
    Auto-generates full REST CRUD interfaces for Course entity management. [cite: 147, 148]
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=["get"])
    def students(self, request, pk=None):
        course = self.get_object()
        enrollments = Enrollment.objects.filter(course=course)
        students = [e.student for e in enrollments]

        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer