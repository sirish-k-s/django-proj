# Generated by Django 4.2.1 on 2023-05-22 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_comment_create_date_alter_post_create_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publised_date',
            new_name='published_date',
        ),
    ]