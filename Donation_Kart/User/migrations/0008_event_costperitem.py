# Generated by Django 2.1 on 2019-04-14 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_event_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='costperitem',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
