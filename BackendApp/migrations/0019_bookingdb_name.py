# Generated by Django 4.1.7 on 2023-07-02 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackendApp', '0018_remove_bookingdb_name_alter_bookingdb_seat'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingdb',
            name='Name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
