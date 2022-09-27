
from django.db.models.aggregates import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework import status
from management.pagination import DefaultPagination
from management.filters import SchoolFilter, StudentFilter
from .models import School, Student
from .serializers import SchoolSerializer, SchoolStudentSerializer, StudentSerializer


class SchoolViewSet(ModelViewSet):
    queryset = School.objects.annotate(
        no_of_students=Count('students')).all()
    serializer_class = SchoolSerializer
    pagination_class = DefaultPagination
    filterset_class = SchoolFilter
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']

    def destroy(self, request, *args, **kwargs):
        if Student.objects.filter(school_id=kwargs['pk']).count() > 0:
            return Response({'error': 'School cannot be deleted because it is associated with students.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = DefaultPagination
    filterset_class = SchoolFilter
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['first_name', 'last_name', 'age',
                    'nationality', 'identification']
    ordering_fields = ['age', 'nationality']

    


class SchoolStudentViewSet(ModelViewSet):
    serializer_class = SchoolStudentSerializer
    pagination_class = DefaultPagination
    filterset_class = StudentFilter
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['first_name', 'last_name', 'age',
                    'nationality', 'identification']
    ordering_fields = ['age', 'nationality']

    def get_queryset(self):
        return Student.objects.filter(school_id=self.kwargs['school_pk'])

    def get_serializer_context(self):
        return {'school_id': self.kwargs['school_pk']}
    
    def create(self, request, *args, **kwargs):
        school_id=self.kwargs['school_pk']
        school = School.objects.annotate(
            no_of_students=Count('students')).get(id=school_id)
        serializer = SchoolSerializer(school)
        if serializer.data['max_students'] > serializer.data['no_of_students']:
            return super().create(request, *args, **kwargs)
        return Response("Max student limit reached", status=status.HTTP_400_BAD_REQUEST)