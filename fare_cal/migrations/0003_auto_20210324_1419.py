# Generated by Django 3.1.7 on 2021-03-24 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fare_cal', '0002_boardingdetails_line_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardingDetail',
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
        migrations.CreateModel(
            name='LineDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_color', models.CharField(max_length=10)),
                ('line_charge', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='BoardingDetails',
        ),
        migrations.AddField(
            model_name='boardingdetail',
            name='line_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fare_cal.linedetail'),
        ),
    ]
