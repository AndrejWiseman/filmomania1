# Generated by Django 5.0.4 on 2024-05-07 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serije', '0009_remove_serije_zanr_serije_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='epizoda',
            name='epizode_preuzmi',
            field=models.CharField(default='', max_length=300),
        ),
    ]
