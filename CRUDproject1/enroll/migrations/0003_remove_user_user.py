# Generated by Django 4.1.7 on 2023-04-22 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_user_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user',
        ),
    ]
