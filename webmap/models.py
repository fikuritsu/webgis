# this is the python code that will generate model in the framework. The models are equivalent to the tables in the PostGIS database

from django.db import models
from django.contrib.gis.db import models as gis_models


# Create your models here.
class PointsOrder(models.Model):
    gid = models.AutoField(primary_key=True)
    id = models.CharField(max_length=7, blank=True, null=True)
    id_shape = models.FloatField(blank=True, null=True)
    id_part = models.FloatField(blank=True, null=True)
    id_point = models.FloatField(blank=True, null=True)
    geom = gis_models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'points_order'

    def __str__(self):
        return self.id

# Create your models here.
class Riverdata(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    geom = gis_models.PointField(blank=True, null=True)
    id_shape = models.FloatField(blank=True, null=True)
    id_part = models.FloatField(blank=True, null=True)
    id_point = models.FloatField(blank=True, null=True)
    id_pk = models.CharField(max_length=10, blank=True, null=True)
    plastic = models.IntegerField(db_column='Plastic', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'riverData'
    
    def __str__(self):
        return self.id


class Att456(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    ele = models.FloatField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    desc = models.CharField(max_length=20, blank=True, null=True)
    sym = models.CharField(max_length=20, blank=True, null=True)
    hdop = models.FloatField(blank=True, null=True)
    locus_icon = models.CharField(max_length=20, blank=True, null=True)
    wkb_geometry = gis_models.PointField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'att_4_56'

    def __str__(self):
        return self.name

class datepicker(models.Model):
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)


class Shop(models.Model):
    name = models.CharField(max_length=100)
    location = gis_models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

class Userlocation(models.Model):
    user_latitude = models.FloatField(blank=True, null=True)
    user_longitude = models.FloatField(blank=True, null=True)

class Hotpoints(models.Model):
    wkb_geometry = gis_models.GeometryField(srid=0, blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hotpoints'




