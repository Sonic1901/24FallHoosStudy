# Generated by Django 4.2.16 on 2024-12-05 06:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hoos_study_app', '0031_merge_20241204_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='studysession',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_sessions', to=settings.AUTH_USER_MODEL),
        ),
    ]
