# Generated by Django 3.2.6 on 2021-09-26 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_rename_image_imagemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='name',
            field=models.CharField(default='Test', max_length=255),
        ),
    ]
