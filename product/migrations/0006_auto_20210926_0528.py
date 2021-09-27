# Generated by Django 3.2.6 on 2021-09-26 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_imagemodel_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagemodel',
            name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_data',
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='product',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='product.product'),
        ),
    ]