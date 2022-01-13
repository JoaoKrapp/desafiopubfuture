# Generated by Django 3.2.5 on 2021-12-14 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(upload_to='avatars/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='background',
            field=models.ImageField(default='background.jpg', upload_to='backgrounds/'),
        ),
    ]
