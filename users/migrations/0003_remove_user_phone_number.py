# Generated by Django 4.2.11 on 2024-05-06 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_experience_alter_user_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
    ]
