# Generated by Django 3.2.9 on 2021-12-06 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAuth', '0003_fraudcheck'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fraudcheck',
            name='time',
            field=models.CharField(max_length=100),
        ),
    ]
