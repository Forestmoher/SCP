# Generated by Django 2.2.5 on 2021-07-27 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Archive', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.ImageField(upload_to='Archive/static/Archive/images/item_images'),
        ),
    ]
