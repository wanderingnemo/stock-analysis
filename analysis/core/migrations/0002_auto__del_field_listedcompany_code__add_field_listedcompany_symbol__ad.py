# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ListedCompany.code'
        db.delete_column('core_listedcompany', 'code')

        # Adding field 'ListedCompany.symbol'
        db.add_column('core_listedcompany', 'symbol',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=10),
                      keep_default=False)

        # Adding field 'ListedCompany.isin'
        db.add_column('core_listedcompany', 'isin',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'ListedCompany.code'
        db.add_column('core_listedcompany', 'code',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=10),
                      keep_default=False)

        # Deleting field 'ListedCompany.symbol'
        db.delete_column('core_listedcompany', 'symbol')

        # Deleting field 'ListedCompany.isin'
        db.delete_column('core_listedcompany', 'isin')


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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isin': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['core']