# Generated by Django 3.1.5 on 2021-01-28 14:54

from django.db import migrations, models
import home.file_upload_utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to=home.file_upload_utils.format_upload_names)),
            ],
        ),
    ]
