# Generated by Django 5.1.1 on 2024-10-06 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_emailaddress_unique_primary_email'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('hoos_study_app', '0005_class_course_students_user_courses_and_more'),
        ('socialaccount', '0006_alter_socialaccount_extra_data'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='CustomUser',
        ),
    ]
