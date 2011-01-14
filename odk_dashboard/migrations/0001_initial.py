# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Phone'
        db.create_table('odk_dashboard_phone', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('device_id', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('most_recent_surveyor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['odk_dashboard.Surveyor'], null=True, blank=True)),
        ))
        db.send_create_signal('odk_dashboard', ['Phone'])

        # Adding model 'GPS'
        db.create_table('odk_dashboard_gps', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('altitude', self.gf('django.db.models.fields.FloatField')()),
            ('accuracy', self.gf('django.db.models.fields.FloatField')()),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['odk_dashboard.District'], null=True, blank=True)),
        ))
        db.send_create_signal('odk_dashboard', ['GPS'])

        # Adding model 'District'
        db.create_table('odk_dashboard_district', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('path', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('depth', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('numchild', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('kml_present', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('latlng_string', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('odk_dashboard', ['District'])

        # Adding model 'SurveyType'
        db.create_table('odk_dashboard_surveytype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('odk_dashboard', ['SurveyType'])

        # Adding model 'Location'
        db.create_table('odk_dashboard_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('gps', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['odk_dashboard.GPS'], null=True, blank=True)),
        ))
        db.send_create_signal('odk_dashboard', ['Location'])

        # Adding model 'ParsedInstance'
        db.create_table('odk_dashboard_parsedinstance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('instance', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['odk_dropbox.Instance'], unique=True)),
            ('survey_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['odk_dashboard.SurveyType'])),
            ('start', self.gf('django.db.models.fields.DateTimeField')()),
            ('end', self.gf('django.db.models.fields.DateTimeField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('surveyor', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='submissions', null=True, to=orm['odk_dashboard.Surveyor'])),
            ('phone', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['odk_dashboard.Phone'])),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['odk_dashboard.Location'], null=True, blank=True)),
        ))
        db.send_create_signal('odk_dashboard', ['ParsedInstance'])

        # Adding model 'Surveyor'
        db.create_table('odk_dashboard_surveyor', (
            ('user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('registration', self.gf('django.db.models.fields.related.ForeignKey')(related_name='surveyor registration', to=orm['odk_dashboard.ParsedInstance'])),
        ))
        db.send_create_signal('odk_dashboard', ['Surveyor'])


    def backwards(self, orm):
        
        # Deleting model 'Phone'
        db.delete_table('odk_dashboard_phone')

        # Deleting model 'GPS'
        db.delete_table('odk_dashboard_gps')

        # Deleting model 'District'
        db.delete_table('odk_dashboard_district')

        # Deleting model 'SurveyType'
        db.delete_table('odk_dashboard_surveytype')

        # Deleting model 'Location'
        db.delete_table('odk_dashboard_location')

        # Deleting model 'ParsedInstance'
        db.delete_table('odk_dashboard_parsedinstance')

        # Deleting model 'Surveyor'
        db.delete_table('odk_dashboard_surveyor')


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
        'odk_dashboard.district': {
            'Meta': {'object_name': 'District'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kml_present': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'latlng_string': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'numchild': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'odk_dashboard.gps': {
            'Meta': {'object_name': 'GPS'},
            'accuracy': ('django.db.models.fields.FloatField', [], {}),
            'altitude': ('django.db.models.fields.FloatField', [], {}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['odk_dashboard.District']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {})
        },
        'odk_dashboard.location': {
            'Meta': {'object_name': 'Location'},
            'gps': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['odk_dashboard.GPS']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'odk_dashboard.parsedinstance': {
            'Meta': {'object_name': 'ParsedInstance'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['odk_dropbox.Instance']", 'unique': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['odk_dashboard.Location']", 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['odk_dashboard.Phone']"}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'survey_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['odk_dashboard.SurveyType']"}),
            'surveyor': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'submissions'", 'null': 'True', 'to': "orm['odk_dashboard.Surveyor']"})
        },
        'odk_dashboard.phone': {
            'Meta': {'object_name': 'Phone'},
            'device_id': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'most_recent_surveyor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['odk_dashboard.Surveyor']", 'null': 'True', 'blank': 'True'})
        },
        'odk_dashboard.surveyor': {
            'Meta': {'object_name': 'Surveyor', '_ormbases': ['auth.User']},
            'registration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'surveyor registration'", 'to': "orm['odk_dashboard.ParsedInstance']"}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        'odk_dashboard.surveytype': {
            'Meta': {'object_name': 'SurveyType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'odk_dropbox.form': {
            'Meta': {'ordering': "('id_string',)", 'object_name': 'Form'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_string': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'xml_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'odk_dropbox.instance': {
            'Meta': {'object_name': 'Instance'},
            'form': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'instances'", 'null': 'True', 'to': "orm['odk_dropbox.Form']"}),
            'hash': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'xml_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['odk_dashboard']