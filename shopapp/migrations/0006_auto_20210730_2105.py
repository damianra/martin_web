# Generated by Django 3.1.12 on 2021-07-31 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0005_promo'),
    ]

    operations = [
        migrations.AddField(
            model_name='promo',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
