# Generated by Django 4.1.7 on 2023-04-07 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_date', models.TimeField()),
                ('event_title', models.CharField(max_length=200)),
                ('event_bullet_1', models.FloatField(help_text='Required')),
                ('event_bullet_2', models.FloatField(help_text='Opional', null=True)),
                ('event_bullet_3', models.FloatField(help_text='Opional', null=True)),
                ('event_bullet_4', models.FloatField(help_text='Opional', null=True)),
                ('event_bullet_5', models.FloatField(help_text='Opional', null=True)),
                ('source1_url', models.URLField(help_text='Required')),
                ('source1_image', models.URLField(help_text='Required')),
                ('source2_url', models.URLField(help_text='Opional', null=True)),
                ('source2_image', models.URLField(help_text='Opional', null=True)),
                ('source3_url', models.URLField(help_text='Opional', null=True)),
                ('source3_image', models.URLField(help_text='Opional', null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
