# Generated by Django 3.2.6 on 2021-09-28 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_imagemodel_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagemodel',
            name='thumbnail',
        ),
    ]
