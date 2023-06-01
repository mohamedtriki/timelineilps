# Generated by Django 4.1.7 on 2023-04-12 23:29

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0007_event_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('GD', 'GD'), ('BD', 'BD'), ('GD/BD', 'GD/BD'), ('LGD', 'LGD'), ('LBD', 'LBD'), ('GrD', 'GrD')], max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='excel_files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, help_text='up to 20 reports', upload_to='')),
                ('user', models.OneToOneField(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
