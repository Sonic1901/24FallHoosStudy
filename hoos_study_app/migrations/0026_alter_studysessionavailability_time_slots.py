# Generated by Django 4.2.16 on 2024-12-03 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoos_study_app', '0025_alter_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studysessionavailability',
            name='time_slots',
            field=models.TextField(default=''),
        ),
    ]