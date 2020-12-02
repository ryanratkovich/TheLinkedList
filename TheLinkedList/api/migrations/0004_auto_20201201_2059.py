# Generated by Django 3.1.3 on 2020-12-02 02:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201201_1722'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='e_name',
            new_name='event_name',
        ),
        migrations.AddField(
            model_name='user',
            name='event',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='event',
            name='endTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='event',
            name='startTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
