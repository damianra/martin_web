# Generated by Django 3.1.12 on 2021-07-30 23:52

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0004_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('picture', models.FileField(default='default.jpg', upload_to='img_products')),
                ('data', jsonfield.fields.JSONField(default=dict)),
            ],
        ),
    ]
