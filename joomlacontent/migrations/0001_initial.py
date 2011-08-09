# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'JosSections'
        db.create_table(u'jos_sections', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('alias', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image', self.gf('django.db.models.fields.TextField')()),
            ('scope', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('image_position', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('published', self.gf('django.db.models.fields.IntegerField')()),
            ('checked_out', self.gf('django.db.models.fields.IntegerField')()),
            ('checked_out_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('ordering', self.gf('django.db.models.fields.IntegerField')()),
            ('access', self.gf('django.db.models.fields.IntegerField')()),
            ('count', self.gf('django.db.models.fields.IntegerField')()),
            ('params', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('joomlacontent', ['JosSections'])

        # Adding model 'JosCategories'
        db.create_table(u'jos_categories', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['joomlacontent.JosCategories'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('alias', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('section', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('image_position', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('published', self.gf('django.db.models.fields.IntegerField')()),
            ('checked_out', self.gf('django.db.models.fields.IntegerField')()),
            ('checked_out_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('editor', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')()),
            ('access', self.gf('django.db.models.fields.IntegerField')()),
            ('count', self.gf('django.db.models.fields.IntegerField')()),
            ('params', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('joomlacontent', ['JosCategories'])

        # Adding model 'JosContentRating'
        db.create_table(u'jos_content_rating', (
            ('content_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('rating_sum', self.gf('django.db.models.fields.IntegerField')()),
            ('rating_count', self.gf('django.db.models.fields.IntegerField')()),
            ('lastip', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('joomlacontent', ['JosContentRating'])

        # Adding model 'JosContent'
        db.create_table(u'jos_content', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('alias', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('title_alias', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('introtext', self.gf('django.db.models.fields.TextField')()),
            ('fulltext', self.gf('django.db.models.fields.TextField')()),
            ('state', self.gf('django.db.models.fields.IntegerField')()),
            ('sectionid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['joomlacontent.JosSections'])),
            ('mask', self.gf('django.db.models.fields.IntegerField')()),
            ('catid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['joomlacontent.JosCategories'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('modified', self.gf('django.db.models.fields.DateTimeField')()),
            ('modified_by', self.gf('django.db.models.fields.IntegerField')()),
            ('checked_out', self.gf('django.db.models.fields.IntegerField')()),
            ('checked_out_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('publish_up', self.gf('django.db.models.fields.DateTimeField')()),
            ('publish_down', self.gf('django.db.models.fields.DateTimeField')()),
            ('images', self.gf('django.db.models.fields.TextField')()),
            ('urls', self.gf('django.db.models.fields.TextField')()),
            ('attribs', self.gf('django.db.models.fields.TextField')()),
            ('version', self.gf('django.db.models.fields.IntegerField')()),
            ('parentid', self.gf('django.db.models.fields.IntegerField')()),
            ('ordering', self.gf('django.db.models.fields.IntegerField')()),
            ('metakey', self.gf('django.db.models.fields.TextField')()),
            ('metadesc', self.gf('django.db.models.fields.TextField')()),
            ('access', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['joomlacontent.JosContentRating'])),
            ('hits', self.gf('django.db.models.fields.IntegerField')()),
            ('metadata', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('joomlacontent', ['JosContent'])

        # Adding model 'JosContentFrontpage'
        db.create_table(u'jos_content_frontpage', (
            ('content_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['joomlacontent.JosContent'], primary_key=True)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('joomlacontent', ['JosContentFrontpage'])


    def backwards(self, orm):
        
        # Deleting model 'JosSections'
        db.delete_table(u'jos_sections')

        # Deleting model 'JosCategories'
        db.delete_table(u'jos_categories')

        # Deleting model 'JosContentRating'
        db.delete_table(u'jos_content_rating')

        # Deleting model 'JosContent'
        db.delete_table(u'jos_content')

        # Deleting model 'JosContentFrontpage'
        db.delete_table(u'jos_content_frontpage')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'joomlacontent.joscategories': {
            'Meta': {'object_name': 'JosCategories', 'db_table': "u'jos_categories'"},
            'access': ('django.db.models.fields.IntegerField', [], {}),
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'checked_out': ('django.db.models.fields.IntegerField', [], {}),
            'checked_out_time': ('django.db.models.fields.DateTimeField', [], {}),
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'editor': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'image_position': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {}),
            'params': ('django.db.models.fields.TextField', [], {}),
            'parent_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['joomlacontent.JosCategories']"}),
            'published': ('django.db.models.fields.IntegerField', [], {}),
            'section': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'joomlacontent.joscontent': {
            'Meta': {'object_name': 'JosContent', 'db_table': "u'jos_content'"},
            'access': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['joomlacontent.JosContentRating']"}),
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'attribs': ('django.db.models.fields.TextField', [], {}),
            'catid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['joomlacontent.JosCategories']"}),
            'checked_out': ('django.db.models.fields.IntegerField', [], {}),
            'checked_out_time': ('django.db.models.fields.DateTimeField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'fulltext': ('django.db.models.fields.TextField', [], {}),
            'hits': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.TextField', [], {}),
            'introtext': ('django.db.models.fields.TextField', [], {}),
            'mask': ('django.db.models.fields.IntegerField', [], {}),
            'metadata': ('django.db.models.fields.TextField', [], {}),
            'metadesc': ('django.db.models.fields.TextField', [], {}),
            'metakey': ('django.db.models.fields.TextField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'modified_by': ('django.db.models.fields.IntegerField', [], {}),
            'ordering': ('django.db.models.fields.IntegerField', [], {}),
            'parentid': ('django.db.models.fields.IntegerField', [], {}),
            'publish_down': ('django.db.models.fields.DateTimeField', [], {}),
            'publish_up': ('django.db.models.fields.DateTimeField', [], {}),
            'sectionid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['joomlacontent.JosSections']"}),
            'state': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_alias': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'urls': ('django.db.models.fields.TextField', [], {}),
            'version': ('django.db.models.fields.IntegerField', [], {})
        },
        'joomlacontent.joscontentfrontpage': {
            'Meta': {'object_name': 'JosContentFrontpage', 'db_table': "u'jos_content_frontpage'"},
            'content_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['joomlacontent.JosContent']", 'primary_key': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {})
        },
        'joomlacontent.joscontentrating': {
            'Meta': {'object_name': 'JosContentRating', 'db_table': "u'jos_content_rating'"},
            'content_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'lastip': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'rating_count': ('django.db.models.fields.IntegerField', [], {}),
            'rating_sum': ('django.db.models.fields.IntegerField', [], {})
        },
        'joomlacontent.jossections': {
            'Meta': {'object_name': 'JosSections', 'db_table': "u'jos_sections'"},
            'access': ('django.db.models.fields.IntegerField', [], {}),
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'checked_out': ('django.db.models.fields.IntegerField', [], {}),
            'checked_out_time': ('django.db.models.fields.DateTimeField', [], {}),
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.TextField', [], {}),
            'image_position': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {}),
            'params': ('django.db.models.fields.TextField', [], {}),
            'published': ('django.db.models.fields.IntegerField', [], {}),
            'scope': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['joomlacontent']
