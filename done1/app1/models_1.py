# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class App1Currency(models.Model):
    name = models.CharField(max_length=8)
    solde = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'app1_currency'


class App1CurrencyPaymethods(models.Model):
    currency = models.ForeignKey(App1Currency, models.DO_NOTHING)
    paymethods = models.ForeignKey('App1Paymethods', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app1_currency_paymethods'
        unique_together = (('currency', 'paymethods'),)


class App1Paymethods(models.Model):
    name = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'app1_paymethods'


class App1Person(models.Model):
    name = models.CharField(max_length=15)
    account = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'app1_person'


class App1Portefeuille(models.Model):
    lumicash = models.IntegerField()
    owner_username = models.CharField(max_length=15)
    owner = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app1_portefeuille'


class App1PortefeuilleCurrency(models.Model):
    portefeuille = models.ForeignKey(App1Portefeuille, models.DO_NOTHING)
    currency = models.ForeignKey(App1Currency, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app1_portefeuille_currency'
        unique_together = (('portefeuille', 'currency'),)


class App1Recharge(models.Model):
    phone = models.IntegerField()
    amount = models.IntegerField()
    code_transaction = models.CharField(max_length=15)
    owner = models.ForeignKey('AuthUser', models.DO_NOTHING)
    date_action = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'app1_recharge'


class App1Requeste(models.Model):
    amount_to_deb = models.IntegerField()
    state_progress = models.IntegerField()
    pay_method = models.IntegerField()
    user_username = models.CharField(max_length=15)
    user_id = models.ForeignKey('AuthUser', models.DO_NOTHING)
    date_approved = models.DateTimeField()
    link_to_activate = models.CharField(max_length=200)
    approved_by = models.CharField(max_length=15)
    amount_to_send = models.IntegerField()
    receiver_number = models.IntegerField()
    date_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'app1_requeste'


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
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

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
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

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
