# Generated by Django 3.1.4 on 2021-08-09 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BLC', '0002_auto_20210808_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=600),
        ),
    ]