# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserSeason'
        db.create_table(u'user_season', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='xseasons', to=orm['series.User'])),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(related_name='xusers', to=orm['series.Season'])),
            ('last_episode_seen', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('last_episode_unfinished', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('season_completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
        ))
        db.send_create_signal(u'series', ['UserSeason'])

        # Adding field 'Season.thetvdb_id'
        db.add_column(u'season', 'thetvdb_id',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Deleting field 'Serial.imdb_url'
        db.delete_column(u'serial', 'imdb_url')

        # Adding field 'Serial.imdb_id'
        db.add_column(u'serial', 'imdb_id',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Serial.thetvdb_id'
        db.add_column(u'serial', 'thetvdb_id',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'User.created'
        db.add_column(u'series_user', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True),
                      keep_default=False)

        # Adding field 'User.modified'
        db.add_column(u'series_user', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'UserSeason'
        db.delete_table(u'user_season')

        # Deleting field 'Season.thetvdb_id'
        db.delete_column(u'season', 'thetvdb_id')

        # Adding field 'Serial.imdb_url'
        db.add_column(u'serial', 'imdb_url',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Deleting field 'Serial.imdb_id'
        db.delete_column(u'serial', 'imdb_id')

        # Deleting field 'Serial.thetvdb_id'
        db.delete_column(u'serial', 'thetvdb_id')

        # Deleting field 'User.created'
        db.delete_column(u'series_user', 'created')

        # Deleting field 'User.modified'
        db.delete_column(u'series_user', 'modified')


    models = {
        u'series.season': {
            'Meta': {'object_name': 'Season', 'db_table': "u'season'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'episode_number': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imdb_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'serial': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'seasons'", 'to': u"orm['series.Serial']"}),
            'thetvdb_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'wikipedia_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
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
            'wikipedia_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
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