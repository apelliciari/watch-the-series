from django.db import models
from django.db.models.query import QuerySet
from django.template.defaultfilters import slugify

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


class Serial(models.Model):
    name = models.CharField(max_length=255, blank=False)
    slug = models.SlugField(max_length=255, blank=False)
    wikipedia_url = models.CharField(max_length=255, blank=True)
    imdb_url = models.CharField(max_length=255, blank=True)
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
            self.slug = slugify(self.slug)

        super(Serial, self).save(*args, **kwargs)

