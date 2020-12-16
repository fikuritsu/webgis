# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class Att1055(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    ele = models.FloatField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    desc = models.CharField(max_length=-1, blank=True, null=True)
    link1_href = models.CharField(max_length=-1, blank=True, null=True)
    sym = models.CharField(max_length=-1, blank=True, null=True)
    hdop = models.FloatField(blank=True, null=True)
    locus_icon = models.CharField(max_length=-1, blank=True, null=True)
    wkb_geometry = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'att_10_55'


class Att1457(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    point = models.CharField(max_length=-1, blank=True, null=True)
    id = models.CharField(max_length=-1, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    note = models.CharField(max_length=-1, blank=True, null=True)
    image = models.CharField(max_length=-1, blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'att_14_57'


class Att145(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    description = models.CharField(max_length=-1, blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'att_1_45'


class Att456(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    ele = models.FloatField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    desc = models.CharField(max_length=-1, blank=True, null=True)
    sym = models.CharField(max_length=-1, blank=True, null=True)
    hdop = models.FloatField(blank=True, null=True)
    locus_icon = models.CharField(max_length=-1, blank=True, null=True)
    wkb_geometry = models.PointField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'att_4_56'


class Att549(models.Model):
    gid = models.AutoField(primary_key=True)
    id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=80, blank=True, null=True)
    geom = models.MultiLineStringField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'att_5_49'


class Att650(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    point = models.CharField(max_length=-1, blank=True, null=True)
    id = models.CharField(max_length=-1, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    note = models.CharField(max_length=-1, blank=True, null=True)
    image = models.CharField(max_length=-1, blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'att_6_50'


class Att853(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    ele = models.FloatField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    desc = models.CharField(max_length=-1, blank=True, null=True)
    link1_href = models.CharField(max_length=-1, blank=True, null=True)
    sym = models.CharField(max_length=-1, blank=True, null=True)
    hdop = models.FloatField(blank=True, null=True)
    locus_icon = models.CharField(max_length=-1, blank=True, null=True)
    wkb_geometry = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'att_8_53'


class Att954(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    ele = models.FloatField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    desc = models.CharField(max_length=-1, blank=True, null=True)
    link1_href = models.CharField(max_length=-1, blank=True, null=True)
    sym = models.CharField(max_length=-1, blank=True, null=True)
    hdop = models.FloatField(blank=True, null=True)
    locus_icon = models.CharField(max_length=-1, blank=True, null=True)
    wkb_geometry = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'att_9_54'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Hotpoints(models.Model):
    wkb_geometry = models.GeometryField(srid=0, blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hotpoints'


class Inventory(models.Model):
    group_id = models.IntegerField(blank=True, null=True)
    filename = models.TextField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory'


class PointsOrder(models.Model):
    gid = models.AutoField(primary_key=True)
    id = models.CharField(max_length=7, blank=True, null=True)
    id_shape = models.FloatField(blank=True, null=True)
    id_part = models.FloatField(blank=True, null=True)
    id_point = models.FloatField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'points_order'


class Riverdata(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    geom = models.PointField(blank=True, null=True)
    id_shape = models.FloatField(blank=True, null=True)
    id_part = models.FloatField(blank=True, null=True)
    id_point = models.FloatField(blank=True, null=True)
    id_pk = models.CharField(max_length=-1, blank=True, null=True)
    plastic = models.IntegerField(db_column='Plastic', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'riverData'


class WebmapDatepicker(models.Model):
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'webmap_datepicker'


class WebmapShop(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'webmap_shop'


class WebmapUserlocation(models.Model):
    user_latitude = models.FloatField(blank=True, null=True)
    user_longitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'webmap_userlocation'
