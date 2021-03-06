# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Season.wikipedia_url'
        db.delete_column(u'season', 'wikipedia_url')

        # Deleting field 'Season.imdb_url'
        db.delete_column(u'season', 'imdb_url')

        # Deleting field 'Serial.wikipedia_url'
        db.delete_column(u'serial', 'wikipedia_url')


    def backwards(self, orm):
        # Adding field 'Season.wikipedia_url'
        db.add_column(u'season', 'wikipedia_url',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Season.imdb_url'
        db.add_column(u'season', 'imdb_url',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Serial.wikipedia_url'
        db.add_column(u'serial', 'wikipedia_url',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)


    models = {
        u'series.season': {
            'Meta': {'object_name': 'Season', 'db_table': "u'season'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'episode_number': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'serial': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'seasons'", 'to': u"orm['series.Serial']"}),
            'thetvdb_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'series.serial': {
            'Meta': {'object_name': 'Serial', 'db_table': "u'serial'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imdb_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'thetvdb_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'thetvdb_last_updated': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'series.user': {
            'Meta': {'object_name': 'User'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'medaglie': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['series.Season']", 'through': u"orm['series.UserSeason']", 'symmetrical': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'series.userseason': {
            'Meta': {'object_name': 'UserSeason', 'db_table': "u'user_season'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_episode_seen': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'last_episode_unfinished': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'xusers'", 'to': u"orm['series.Season']"}),
            'season_completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'xseasons'", 'to': u"orm['series.User']"})
        }
    }

    complete_apps = ['series']