# Generated by Django 3.1.4 on 2020-12-21 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201208_1925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newuser',
            old_name='username',
            new_name='user_name',
        ),
    ]
