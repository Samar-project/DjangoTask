# Generated by Django 4.2.10 on 2024-02-29 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0002_alter_trip_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='user_id',
            field=models.CharField(max_length=15, verbose_name='usid'),
        ),
    ]
