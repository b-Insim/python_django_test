# Generated by Django 2.1.7 on 2020-06-03 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('contacted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=200, unique=True)),
                ('description', models.CharField(max_length=200)),
                ('available', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('picture', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='References',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.CharField(max_length=200)),
                ('biere', models.ManyToManyField(blank=True, related_name='biere', to='telecom.Biere')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telecom.Contact'),
        ),
        migrations.AddField(
            model_name='booking',
            name='menu',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='telecom.Menu'),
        ),
    ]