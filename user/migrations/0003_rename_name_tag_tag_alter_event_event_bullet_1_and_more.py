# Generated by Django 4.1.7 on 2023-04-07 07:30

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0002_event_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='name',
            new_name='tag',
        ),
        migrations.AlterField(
            model_name='event',
            name='event_bullet_1',
            field=models.CharField(help_text='Required', max_length=200),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_bullet_2',
            field=models.CharField(blank=True, help_text='Opional', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_bullet_3',
            field=models.CharField(blank=True, help_text='Opional', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_bullet_4',
            field=models.CharField(blank=True, help_text='Opional', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_bullet_5',
            field=models.CharField(blank=True, help_text='Opional', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='source2_image',
            field=models.URLField(blank=True, help_text='Opional', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='source2_url',
            field=models.URLField(blank=True, help_text='Opional', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='source3_image',
            field=models.URLField(blank=True, help_text='Opional', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='source3_url',
            field=models.URLField(blank=True, help_text='Opional', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='user',
            field=models.OneToOneField(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
