# Generated by Django 3.1.2 on 2020-10-31 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pg', '0018_videoe'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoe',
            name='softwaretype',
            field=models.CharField(choices=[('', ''), ('film editing software', 'film editing software'), ('composting tool', 'composting tool'), ('3d tool', '3d tool'), ('color grading tool', 'color grading tool'), ('rendering tool', 'rendering tool')], default='new', max_length=100),
        ),
    ]
