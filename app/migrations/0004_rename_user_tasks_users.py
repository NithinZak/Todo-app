# Generated by Django 4.2.6 on 2023-10-29 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_tasks_options_rename_complete_tasks_completed_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='user',
            new_name='users',
        ),
    ]
