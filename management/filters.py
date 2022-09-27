from django_filters.rest_framework import FilterSet
from .models import School, Student


class SchoolFilter(FilterSet):
    class Meta:
        model = School
        fields = {
            'name': ['exact'],
        }


class StudentFilter(FilterSet):
    class Meta:
        model = Student
        fields = {
            'first_name': ['exact'],
            'last_name': ['exact'],
            'age': ['gt', 'lt'],
            'identification':['exact'] 
        }