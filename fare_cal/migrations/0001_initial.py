# Generated by Django 3.1.7 on 2021-03-24 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardingDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boarding_name', models.CharField(max_length=20)),
                ('is_terminal', models.BooleanField(default=False)),
                ('is_interchange', models.BooleanField(default=False)),
                ('is_bus', models.BooleanField(default=False)),
                ('is_railway', models.BooleanField(default=False)),
                ('is_shuttle', models.BooleanField(default=False)),
                ('is_interchange_terminal', models.BooleanField(default=False)),
            ],
        ),
    ]
