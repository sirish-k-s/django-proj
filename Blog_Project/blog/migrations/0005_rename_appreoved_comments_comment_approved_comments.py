# Generated by Django 4.2.1 on 2023-05-24 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_create_date_comment_created_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='appreoved_comments',
            new_name='approved_comments',
        ),
    ]
