# Generated by Django 3.1.2 on 2020-10-29 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pg', '0010_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
