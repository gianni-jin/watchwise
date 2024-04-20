# Generated by Django 4.2.11 on 2024-04-10 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchwise', '0016_alter_movie_status_alter_tvshow_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tvshow',
            name='first_air_date',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
