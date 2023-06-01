# Generated by Django 4.1.7 on 2023-04-12 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_rename_name_tag_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('GD', 'GD'), ('BD', 'BD'), ('GD/BD', 'GD/BD'), ('LGD', 'LGD'), ('LBD', 'LBD')], default='none', max_length=200),
        ),
    ]