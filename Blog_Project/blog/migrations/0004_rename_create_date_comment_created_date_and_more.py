# Generated by Django 4.2.1 on 2023-05-22 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_publised_date_post_published_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='create_date',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='create_date',
            new_name='created_date',
        ),
    ]
