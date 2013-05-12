# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'UserSeason'
        db.delete_table(u'user_season')

        # Adding field 'UserSerial.current_season'
        db.add_column(u'user_serial', 'current_season',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='x_user_serials', null=True, to=orm['series.Season']),
                      keep_default=False)

        # Adding field 'UserSerial.last_episode_seen'
        db.add_column(u'user_serial', 'last_episode_seen',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'UserSerial.last_episode_unfinished'
        db.add_column(u'user_serial', 'last_episode_unfinished',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'UserSeason'
        db.create_table(u'user_season', (
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(related_name='xusers', to=orm['series.Season'])),
            ('season_completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='xseasons', to=orm['series.User'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('last_episode_unfinished', self.gf('django.db.models.fields.BooleanField')(default=False)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('last_episode_seen', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'series', ['UserSeason'])

        # Deleting field 'UserSerial.current_season'
        db.delete_column(u'user_serial', 'current_season_id')

        # Deleting field 'UserSerial.last_episode_seen'
        db.delete_column(u'user_serial', 'last_episode_seen')

        # Deleting field 'UserSerial.last_episode_unfinished'
        db.delete_column(u'user_serial', 'last_episode_unfinished')


    models = {
        u'series.language': {
            'Meta': {'object_name': 'Language', 'db_table': "u'language'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
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
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'serials': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['series.Serial']", 'through': u"orm['series.UserSerial']", 'symmetrical': 'False'})
        },
        u'series.userserial': {
            'Meta': {'object_name': 'UserSerial', 'db_table': "u'user_serial'"},
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'current_season': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'x_user_serials'", 'null': 'True', 'to': u"orm['series.Season']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['series.Language']"}),
            'last_episode_seen': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'last_episode_unfinished': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'serial': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'x_users'", 'to': u"orm['series.Serial']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'x_serials'", 'to': u"orm['series.User']"})
        }
    }

    complete_apps = ['series']