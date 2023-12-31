# Generated by Django 4.1.7 on 2023-06-19 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackendApp', '0012_bookingdb_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingdb',
            name='Date',
        ),
        migrations.RemoveField(
            model_name='bookingdb',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='bookingdb',
            name='Mobile',
        ),
        migrations.AddField(
            model_name='bookingdb',
            name='Seat',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bookingdb',
            name='Movie',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
