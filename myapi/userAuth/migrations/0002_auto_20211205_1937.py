# Generated by Django 3.2.9 on 2021-12-06 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userAuth', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='fingerPrint',
            new_name='fingerprint',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='userName',
            new_name='username',
        ),
    ]
