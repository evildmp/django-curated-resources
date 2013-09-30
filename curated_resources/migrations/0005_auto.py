# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field curators on 'Resource'
        db.create_table('curated_resources_resource_curators', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('resource', models.ForeignKey(orm['curated_resources.resource'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('curated_resources_resource_curators', ['resource_id', 'user_id'])

        # Adding M2M table for field curators on 'Topic'
        db.create_table('curated_resources_topic_curators', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('topic', models.ForeignKey(orm['curated_resources.topic'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('curated_resources_topic_curators', ['topic_id', 'user_id'])

        # Adding M2M table for field curators on 'Domain'
        db.create_table('curated_resources_domain_curators', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('domain', models.ForeignKey(orm['curated_resources.domain'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('curated_resources_domain_curators', ['domain_id', 'user_id'])

        # Adding M2M table for field curators on 'Audience'
        db.create_table('curated_resources_audience_curators', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('audience', models.ForeignKey(orm['curated_resources.audience'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('curated_resources_audience_curators', ['audience_id', 'user_id'])


    def backwards(self, orm):
        # Removing M2M table for field curators on 'Resource'
        db.delete_table('curated_resources_resource_curators')

        # Removing M2M table for field curators on 'Topic'
        db.delete_table('curated_resources_topic_curators')

        # Removing M2M table for field curators on 'Domain'
        db.delete_table('curated_resources_domain_curators')

        # Removing M2M table for field curators on 'Audience'
        db.delete_table('curated_resources_audience_curators')


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
        'curated_resources.audience': {
            'Meta': {'object_name': 'Audience'},
            'curators': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'curated_resource_audiences'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'curated_resources.domain': {
            'Meta': {'object_name': 'Domain'},
            'curators': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'curated_resource_domains'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
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
            'curators': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'curated_resource_resources'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'destination_content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'links_to_resource'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'destination_object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'domains': ('mptt.fields.TreeManyToManyField', [], {'blank': 'True', 'related_name': "'resources'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['curated_resources.Domain']"}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'related_to': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'related_to_rel_+'", 'null': 'True', 'to': "orm['curated_resources.Resource']"}),
            'resource_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'resources'", 'to': "orm['curated_resources.ResourceType']"}),
            'short_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': 'datetime.datetime(2013, 3, 21, 0, 0)', 'unique': 'True', 'max_length': '75'}),
            'suitable_for': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'resources'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['curated_resources.Audience']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'topics': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'resources'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['curated_resources.Topic']"})
        },
        'curated_resources.resourcetype': {
            'Meta': {'object_name': 'ResourceType'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resource_type': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'curated_resources.topic': {
            'Meta': {'object_name': 'Topic'},
            'curators': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'curated_resource_topics'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['curated_resources']