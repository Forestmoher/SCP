# Generated by Django 2.2.5 on 2021-07-29 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Archive', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='containment_procedure',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_description',
            field=models.CharField(max_length=2000),
        ),
    ]
