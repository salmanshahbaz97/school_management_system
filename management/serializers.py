from rest_framework import serializers
from .models import School, Student


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'students_of_count']

    students_of_count = serializers.IntegerField(read_only=True)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name',
                  'nationality', 'age', 'identification', 'school']

    identification = serializers.UUIDField(read_only=True)


class SchoolStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name',
                  'nationality', 'age', 'identification']

    identification = serializers.UUIDField(read_only=True)

    def create(self, validated_data):
        school_id = self.context['school_id']
        return Student.objects.create(school_id=school_id, **validated_data)