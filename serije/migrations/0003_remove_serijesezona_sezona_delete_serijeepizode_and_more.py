# Generated by Django 5.0.4 on 2024-04-22 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serije', '0002_serijesezona_serijeepizode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serijesezona',
            name='sezona',
        ),
        migrations.DeleteModel(
            name='SerijeEpizode',
        ),
        migrations.DeleteModel(
            name='SerijeSezona',
        ),
    ]
