# Generated by Django 3.1.2 on 2020-10-22 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainman',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
