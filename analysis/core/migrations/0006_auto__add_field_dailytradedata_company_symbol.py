# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DailyTradeData.company_symbol'
        db.add_column('core_dailytradedata', 'company_symbol',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'DailyTradeData.company_symbol'
        db.delete_column('core_dailytradedata', 'company_symbol')


    models = {
        'core.dailytradedata': {
            'Meta': {'object_name': 'DailyTradeData'},
            'close_minus_open': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '9', 'decimal_places': '2'}),
            'close_value': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '9', 'decimal_places': '2'}),
            'company_symbol': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'high_minus_low': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '9', 'decimal_places': '2'}),
            'high_minus_open': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '9', 'decimal_places': '2'}),
            'high_value': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '9', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listed_company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ListedCompany']"}),
            'low_value': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '9', 'decimal_places': '2'}),
            'ltp_value': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '9', 'decimal_places': '2'}),
            'open_value': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '9', 'decimal_places': '2'}),
            'traded_date': ('django.db.models.fields.DateField', [], {}),
            'turn_over': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '16', 'decimal_places': '2'}),
            'volume': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '16', 'decimal_places': '2'})
        },
        'core.listedcompany': {
            'Meta': {'object_name': 'ListedCompany'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isin': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['core']