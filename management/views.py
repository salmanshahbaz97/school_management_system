
from django.db.models.aggregates import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from management.pagination import DefaultPagination
from management.filters import SchoolFilter
from .models import School, Student
from .serializers import SchoolSerializer, SchoolStudentSerializer, StudentSerializer


class SchoolViewSet(ModelViewSet):
    queryset = School.objects.annotate(
        students_of_count=Count('students')).all()
    serializer_class = SchoolSerializer
    pagination_class = DefaultPagination
    filterset_class = SchoolFilter
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class SchoolStudentViewSet(ModelViewSet):
    serializer_class = SchoolStudentSerializer

    def get_queryset(self):
        return Student.objects.filter(school_id=self.kwargs['school_pk'])

    def get_serializer_context(self):
        return {'school_id': self.kwargs['school_pk']}
    
    def create(self, request, *args, **kwargs):
        school_id=self.kwargs['school_pk']
        queryset = School.objects.annotate(
        students_of_count=Count('students')).get(school_id=school_id)
