# Generated by Django 3.2.13 on 2022-06-20 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_num',
            field=models.CharField(max_length=7),
        ),
    ]
