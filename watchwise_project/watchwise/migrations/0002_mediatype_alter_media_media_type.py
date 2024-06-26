# Generated by Django 5.0.3 on 2024-03-20 10:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchwise', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='media',
            name='media_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watchwise.mediatype'),
        ),
    ]
