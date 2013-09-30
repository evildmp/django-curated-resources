# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Resource'
        db.create_table('curated_resources_resource', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('short_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('resource_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['curated_resources.ResourceType'])),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
            ('destination_content_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='links_to_resource', null=True, to=orm['contenttypes.ContentType'])),
            ('destination_object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('curated_resources', ['Resource'])

        # Adding M2M table for field related_to on 'Resource'
        db.create_table('curated_resources_resource_related_to', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_resource', models.ForeignKey(orm['curated_resources.resource'], null=False)),
            ('to_resource', models.ForeignKey(orm['curated_resources.resource'], null=False))
        ))
        db.create_unique('curated_resources_resource_related_to', ['from_resource_id', 'to_resource_id'])

        # Adding M2M table for field suitable_for on 'Resource'
        db.create_table('curated_resources_resource_suitable_for', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('resource', models.ForeignKey(orm['curated_resources.resource'], null=False)),
            ('audience', models.ForeignKey(orm['curated_resources.audience'], null=False))
        ))
        db.create_unique('curated_resources_resource_suitable_for', ['resource_id', 'audience_id'])

        # Adding M2M table for field topics on 'Resource'
        db.create_table('curated_resources_resource_topics', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('resource', models.ForeignKey(orm['curated_resources.resource'], null=False)),
            ('topic', models.ForeignKey(orm['curated_resources.topic'], null=False))
        ))
        db.create_unique('curated_resources_resource_topics', ['resource_id', 'topic_id'])

        # Adding M2M table for field domains on 'Resource'
        db.create_table('curated_resources_resource_domains', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('resource', models.ForeignKey(orm['curated_resources.resource'], null=False)),
            ('domain', models.ForeignKey(orm['curated_resources.domain'], null=False))
        ))
        db.create_unique('curated_resources_resource_domains', ['resource_id', 'domain_id'])

        # Adding model 'ResourceType'
        db.create_table('curated_resources_resourcetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('resource_type', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal('curated_resources', ['ResourceType'])

        # Adding model 'Audience'
        db.create_table('curated_resources_audience', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('curated_resources', ['Audience'])

        # Adding model 'Topic'
        db.create_table('curated_resources_topic', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('curated_resources', ['Topic'])

        # Adding model 'Domain'
        db.create_table('curated_resources_domain', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['curated_resources.Domain'])),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('curated_resources', ['Domain'])


    def backwards(self, orm):
        # Deleting model 'Resource'
        db.delete_table('curated_resources_resource')

        # Removing M2M table for field related_to on 'Resource'
        db.delete_table('curated_resources_resource_related_to')

        # Removing M2M table for field suitable_for on 'Resource'
        db.delete_table('curated_resources_resource_suitable_for')

        # Removing M2M table for field topics on 'Resource'
        db.delete_table('curated_resources_resource_topics')

        # Removing M2M table for field domains on 'Resource'
        db.delete_table('curated_resources_resource_domains')

        # Deleting model 'ResourceType'
        db.delete_table('curated_resources_resourcetype')

        # Deleting model 'Audience'
        db.delete_table('curated_resources_audience')

        # Deleting model 'Topic'
        db.delete_table('curated_resources_topic')

        # Deleting model 'Domain'
        db.delete_table('curated_resources_domain')


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
            'description': ('django.db.models.fields.TextField', [], {}),
            'destination_content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'links_to_resource'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'destination_object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'domains': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['curated_resources.Domain']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'related_to': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'related_to_rel_+'", 'null': 'True', 'to': "orm['curated_resources.Resource']"}),
            'resource_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['curated_resources.ResourceType']"}),
            'short_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
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