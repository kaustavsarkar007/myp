# Generated by Django 4.1.1 on 2022-12-19 12:39

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0002_alter_cricpost_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cricpost',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]