# Generated by Django 3.1.2 on 2020-10-30 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pg', '0013_auto_20201030_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
