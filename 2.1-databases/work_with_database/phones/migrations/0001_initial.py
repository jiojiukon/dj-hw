# Generated by Django 4.1.5 on 2023-02-18 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('price', models.CharField(max_length=40)),
                ('image', models.CharField(max_length=40)),
                ('release_date', models.DateField(max_length=40)),
                ('lte_exists', models.CharField(max_length=40)),
                ('slug', models.SlugField(max_length=300)),
            ],
        ),
    ]
