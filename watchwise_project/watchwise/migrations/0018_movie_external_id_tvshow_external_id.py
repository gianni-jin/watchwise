# Generated by Django 4.2.11 on 2024-04-10 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchwise', '0017_alter_movie_release_date_alter_tvshow_first_air_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='external_id',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='tvshow',
            name='external_id',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
