# Generated by Django 3.0.4 on 2020-03-16 01:03

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
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=255, verbose_name='job title')),
                ('company_name', models.CharField(max_length=255, verbose_name='company name')),
                ('job_role', models.CharField(max_length=255, verbose_name='job role')),
                ('date_started', models.DateField(blank=True, verbose_name='date started')),
                ('date_ended', models.DateField(blank=True, verbose_name='date ended')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'experience',
                'verbose_name_plural': "experience's",
                'db_table': 'experience',
            },
        ),
    ]
