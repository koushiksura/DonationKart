# Generated by Django 2.1 on 2019-04-13 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userlogin', '0002_profile_usertype'),
        ('User', '0004_auto_20190414_0046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('donationid', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('transactionid', models.CharField(max_length=50)),
                ('item', models.CharField(max_length=10)),
                ('Quantity', models.PositiveIntegerField(default=0)),
                ('description', models.CharField(max_length=200)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userlogin.Profile')),
            ],
        ),
    ]
