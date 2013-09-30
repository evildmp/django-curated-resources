# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Resource.slug'
        db.add_column('curated_resources_resource', 'slug',
                      self.gf('django.db.models.fields.SlugField')(unique=False, max_length=75),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Resource.slug'
        db.delete_column('curated_resources_resource', 'slug')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'curated_resources.audience': {
            'Meta': {'object_name': 'Audience'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'curated_resources.domain': {
            'Meta': {'object_name': 'Domain'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['curated_resources.Domain']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'curated_resources.resource': {
            'Meta': {'object_name': 'Resource'},
            'cost': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'destination_content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'links_to_resource'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'destination_object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'domains': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['curated_resources.Domain']", 'null': 'True', 'blank': 'True'}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'related_to': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'related_to_rel_+'", 'null': 'True', 'to': "orm['curated_resources.Resource']"}),
            'resource_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['curated_resources.ResourceType']"}),
            'short_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '75'}),
            'suitable_for': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['curated_resources.Audience']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'topics': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'resources'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['curated_resources.Topic']"})
        },
        'curated_resources.resourcetype': {
            'Meta': {'object_name': 'ResourceType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resource_type': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'curated_resources.topic': {
            'Meta': {'object_name': 'Topic'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['curated_resources']