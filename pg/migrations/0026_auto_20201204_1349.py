# Generated by Django 3.1.3 on 2020-12-04 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pg', '0025_auto_20201203_2013'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='resumes')),
            ],
        ),
        migrations.RemoveField(
            model_name='mainman',
            name='file',
        ),
    ]
