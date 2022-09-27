from django.db import models
from uuid import uuid4
from django.core.validators import MinValueValidator, MaxValueValidator


class School(models.Model):
    name = models.CharField(max_length=20)
    max_students = models.PositiveBigIntegerField(default=0)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    nationality = models.CharField(max_length=255)
    age = models.IntegerField(validators=[MinValueValidator(1)])
    identification = models.UUIDField(default=uuid4)
    school = models.ForeignKey(
        School, on_delete=models.PROTECT, related_name='students')

    def __str__(self) -> str:
        return self.first_name

    class Meta:
        ordering = ['age']