# Generated by Django 5.0.3 on 2024-05-05 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermaster',
            name='usertype',
            field=models.CharField(max_length=30),
        ),
    ]
