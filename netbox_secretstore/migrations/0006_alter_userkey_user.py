# Generated by Django 4.0.8 on 2022-12-28 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('netbox_secretstore', '0005_alter_secret_created_alter_secret_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userkey',
            name='user',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='netbox_secretstore_userkey', to=settings.AUTH_USER_MODEL),
        ),
    ]
