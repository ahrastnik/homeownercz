# Generated by Django 4.2.4 on 2023-08-24 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('price', models.CharField(max_length=128)),
                ('locality', models.CharField(max_length=128)),
                ('url', models.SlugField(max_length=256, unique=True)),
                ('image_url', models.SlugField(max_length=512)),
            ],
        ),
    ]