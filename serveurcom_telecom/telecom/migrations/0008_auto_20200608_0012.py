# Generated by Django 2.1.7 on 2020-06-07 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telecom', '0007_auto_20200608_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comptoir',
            name='name',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
        migrations.AlterField(
            model_name='reference',
            name='name',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='name',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
        migrations.AlterField(
            model_name='stock',
            name='name',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
    ]
