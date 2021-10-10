# Generated by Django 3.2.7 on 2021-10-10 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='biography',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(null=True, related_name='_users_profile_followers_+', to='users.Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(null=True, related_name='_users_profile_following_+', to='users.Profile'),
        ),
    ]
