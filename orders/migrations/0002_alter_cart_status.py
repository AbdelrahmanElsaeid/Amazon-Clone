# Generated by Django 3.2 on 2023-02-26 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(choices=[('Inprogress', 'Inprogress'), ('Completed', 'Completed')], max_length=12),
        ),
    ]
