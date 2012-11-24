# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ListedCompany'
        db.create_table('core_listedcompany', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('core', ['ListedCompany'])

        # Adding model 'DailyTradeData'
        db.create_table('core_dailytradedata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('listed_company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ListedCompany'])),
            ('traded_date', self.gf('django.db.models.fields.DateField')()),
            ('open_value', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=9, decimal_places=2)),
            ('high_value', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=9, decimal_places=2)),
            ('low_value', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=9, decimal_places=2)),
            ('ltp_value', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=9, decimal_places=2)),
            ('close_value', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=9, decimal_places=2)),
            ('volume', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=16, decimal_places=2)),
            ('turn_over', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=16, decimal_places=2)),
            ('high_to_low', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=9, decimal_places=2)),
            ('high_to_open', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=9, decimal_places=2)),
            ('open_to_close', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=9, decimal_places=2)),
        ))
        db.send_create_signal('core', ['DailyTradeData'])


    def backwards(self, orm):
        # Deleting model 'ListedCompany'
        db.delete_table('core_listedcompany')

        # Deleting model 'DailyTradeData'
        db.delete_table('core_dailytradedata')


    models = {
        'core.dailytradedata': {
            'Meta': {'object_name': 'DailyTradeData'},
            'close_value': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '9', 'decimal_places': '2'}),
            'high_to_low': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '9', 'decimal_places': '2'}),
            'high_to_open': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '9', 'decimal_places': '2'}),
            'high_value': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '9', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listed_company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ListedCompany']"}),
            'low_value': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '9', 'decimal_places': '2'}),
            'ltp_value': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '9', 'decimal_places': '2'}),
            'open_to_close': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '9', 'decimal_places': '2'}),
            'open_value': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '9', 'decimal_places': '2'}),
            'traded_date': ('django.db.models.fields.DateField', [], {}),
            'turn_over': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '16', 'decimal_places': '2'}),
            'volume': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '16', 'decimal_places': '2'})
        },
        'core.listedcompany': {
            'Meta': {'object_name': 'ListedCompany'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['core']