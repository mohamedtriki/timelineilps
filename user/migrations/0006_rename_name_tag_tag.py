# Generated by Django 4.1.7 on 2023-04-07 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_rename_tag_name_tag_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='name',
            new_name='tag',
        ),
    ]
