# Generated by Django 2.0.6 on 2019-05-27 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BhpUsers',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role_username', models.CharField(default='', max_length=225, unique=True)),
                ('role_email', models.EmailField(max_length=254, unique=True)),
                ('role_password', models.CharField(max_length=225, unique=True)),
            ],
        ),
    ]
