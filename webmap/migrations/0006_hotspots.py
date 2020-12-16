# Generated by Django 3.1.4 on 2020-12-10 20:07

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webmap', '0005_auto_20201211_0234'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotspots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('wkb_geometry', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('volume', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'hotspots',
                'managed': False,
            },
        ),
    ]