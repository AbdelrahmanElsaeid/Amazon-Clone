# Generated by Django 3.2 on 2023-02-26 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_cart_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='oredrdetail',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
