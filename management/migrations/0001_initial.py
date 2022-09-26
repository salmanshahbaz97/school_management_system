# Generated by Django 4.1.1 on 2022-09-26 09:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=255)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('identification', models.UUIDField(default=uuid.uuid4)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='students', to='management.school')),
            ],
            options={
                'ordering': ['age'],
            },
        ),
        migrations.AddField(
            model_name='school',
            name='max_students',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='management.student'),
        ),
    ]