# Generated by Django 4.1 on 2022-08-11 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster_image',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
