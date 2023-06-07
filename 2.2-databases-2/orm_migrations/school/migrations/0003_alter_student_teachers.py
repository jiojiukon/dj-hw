# Generated by Django 4.1.5 on 2023-06-07 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_remove_student_teacher_student_teachers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(related_name='students', to='school.teacher', verbose_name='Учителя'),
        ),
    ]
