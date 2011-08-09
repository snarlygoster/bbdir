# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Entry.location'
        db.add_column('bbdir_entry', 'location', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True), keep_default=False)

        # Adding field 'Entry.modified'
        db.add_column('bbdir_entry', 'modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True), keep_default=False)

        # Adding field 'Entry.created'
        db.add_column('bbdir_entry', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Entry.location'
        db.delete_column('bbdir_entry', 'location')

        # Deleting field 'Entry.modified'
        db.delete_column('bbdir_entry', 'modified')

        # Deleting field 'Entry.created'
        db.delete_column('bbdir_entry', 'created')


    models = {
        'bbdir.entry': {
            'Meta': {'ordering': "['name', 'city', 'state']", 'object_name': 'Entry'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['bbdir']
