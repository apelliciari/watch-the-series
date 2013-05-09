# -*- coding: utf-8 -*-

from django.db import models
from django.db.models.query import QuerySet
from django.template.defaultfilters import slugify
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from django_extensions.db.fields \
    import CreationDateTimeField, ModificationDateTimeField


def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None

def queryset_get_or_none(model, queryset, **kwargs):
    try:
        return queryset.get(**kwargs)
    except model.DoesNotExist:
        return None

class QuerySetManager(models.Manager):

    def get_query_set(self):
        return self.model.QuerySet(self.model)

    def __getattr__(self, attr, *args):
        return getattr(self.get_query_set(), attr, *args)

class Language(models.Model):
    name = models.CharField(max_length=255, blank=False)
    iso = models.CharField(max_length=10, blank=True, null=True)
    created = CreationDateTimeField(null=True, blank=True)
    modified = ModificationDateTimeField(null=True, blank=True)
    objects = QuerySetManager()

    class QuerySet(QuerySet):
        pass

    class Meta:
        db_table = u'language'
        verbose_name_plural = u'languages'

    def __unicode__(self):
        return self.name

class Serial(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=500, blank=True, null=True)
    slug = models.SlugField(max_length=255, blank=False)
    imdb_id = models.CharField(max_length=255, blank=True)
    thetvdb_id = models.IntegerField(null=True)
    thetvdb_last_updated = models.IntegerField(null=True)
    created = CreationDateTimeField(null=True, blank=True)
    modified = ModificationDateTimeField(null=True, blank=True)
    objects = QuerySetManager()

    class QuerySet(QuerySet):
        pass

    class Meta:
        db_table = u'serial'
        verbose_name_plural = u'series'

    def __unicode__(self):
        return self.name

    #def url(self):
        #return reverse('tag', args=[self.parametro])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = "{slug}-{this.id}".format(slug=slugify(self.name), this=self)

        super(Serial, self).save(*args, **kwargs)

class Season(models.Model):
    number = models.IntegerField(null=False, blank=False)
    serial = models.ForeignKey(Serial, related_name="seasons")
    episode_number = models.IntegerField()
    thetvdb_id = models.IntegerField(null=True)
    created = CreationDateTimeField(null=True, blank=True)
    modified = ModificationDateTimeField(null=True, blank=True)
    objects = QuerySetManager()

    class QuerySet(QuerySet):
        pass

    class Meta:
        db_table = u'season'
        verbose_name_plural = u'seasons'

    def __unicode__(self):
        return "{this.serial} #{this.number} Season, with {this.episode_number} episodes".format(this=self)

    #def url(self):
        #return reverse('tag', args=[self.parametro])

    #def save(self, *args, **kwargs):
        #if not self.slug:
            #self.slug = slugify(self.slug)

        #super(Serial, self).save(*args, **kwargs)

class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=UserManager.normalize_email(email),
            full_name=full_name,
        )

        user.set_password(password)
        #user.save(using=self._db)
        user.save()
        return user

    def create_superuser(self, email, full_name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
            full_name=full_name,
        )
        user.is_admin = True
        user.save()
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        db_index=True,
    )

    full_name = models.CharField(max_length=255, blank=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created = CreationDateTimeField(null=True, blank=True)
    modified = ModificationDateTimeField(null=True, blank=True)
    seasons = models.ManyToManyField('Season', through='UserSeason')
    serials = models.ManyToManyField('Serial', through='UserSerial')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.full_name

    def __unicode__(self):
        return "{this.full_name} <{this.email}>".format(this=self)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class UserSerial(models.Model):

    user = models.ForeignKey(User, related_name = "xserials")
    serial = models.ForeignKey(Serial, related_name = "xusers")
    language = models.ForeignKey(Language)
    completed = models.BooleanField(default=False)
    created = CreationDateTimeField(null=True, blank=True)
    modified = ModificationDateTimeField(null=True, blank=True)

    class Meta:
        db_table = u'user_serial'
        verbose_name_plural = u'users_series'

class UserSeason(models.Model):
    user = models.ForeignKey(User, related_name = "xseasons")
    season = models.ForeignKey(Season, related_name = "xusers")
    last_episode_seen = models.IntegerField(null=True)
    last_episode_unfinished = models.BooleanField(default=False)
    season_completed = models.BooleanField(default=False)
    created = CreationDateTimeField(null=True, blank=True)
    modified = ModificationDateTimeField(null=True, blank=True)

    class Meta:
        db_table = u'user_season'
        verbose_name_plural = u'users_seasons'

