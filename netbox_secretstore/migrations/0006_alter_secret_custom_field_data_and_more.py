# Generated by Django 4.1.4 on 2023-01-24 19:50

from django.db import migrations, models
import utilities.json


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_secretstore', '0005_alter_secret_created_alter_secret_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secret',
            name='custom_field_data',
            field=models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder),
        ),
        migrations.AlterField(
            model_name='secretrole',
            name='custom_field_data',
            field=models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder),
        ),
    ]
