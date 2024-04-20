# Generated by Django 5.0.3 on 2024-03-20 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('media_type', models.CharField(max_length=10)),
                ('release_date', models.DateField()),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
    ]
