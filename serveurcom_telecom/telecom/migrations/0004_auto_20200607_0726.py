# Generated by Django 2.1.7 on 2020-06-07 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telecom', '0003_auto_20200604_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comptoir',
            name='description',
        ),
        migrations.RemoveField(
            model_name='comptoir',
            name='name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='description',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='name',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='ref',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='description',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='name',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='ref',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='ref',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='description',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='name',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='ref',
        ),
    ]