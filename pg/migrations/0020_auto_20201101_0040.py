# Generated by Django 3.1.2 on 2020-10-31 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pg', '0019_videoe_softwaretype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoe',
            name='price',
            field=models.CharField(max_length=100),
        ),
    ]
