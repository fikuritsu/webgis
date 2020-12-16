# Generated by Django 3.1.4 on 2020-12-10 20:33

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webmap', '0007_delete_hotspots'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotpoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wkb_geometry', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=0)),
                ('volume', models.FloatField(blank=True, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'hotpoints',
                'managed': False,
            },
        ),
    ]
