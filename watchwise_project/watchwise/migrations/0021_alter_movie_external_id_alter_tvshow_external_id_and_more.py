# Generated by Django 4.2.11 on 2024-04-13 23:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('watchwise', '0020_movie_user_tvshow_user_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='external_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tvshow',
            name='external_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='movie',
            unique_together={('user', 'external_id')},
        ),
        migrations.AlterUniqueTogether(
            name='tvshow',
            unique_together={('user', 'external_id')},
        ),
    ]