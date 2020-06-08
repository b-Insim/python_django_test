# Generated by Django 2.1.7 on 2020-06-07 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telecom', '0010_auto_20200608_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comptoir',
            name='description',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='description',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='description',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='reference',
            name='description',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='description',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='description',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
