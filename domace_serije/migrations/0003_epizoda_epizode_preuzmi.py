# Generated by Django 5.0.4 on 2024-05-07 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domace_serije', '0002_epizoda'),
    ]

    operations = [
        migrations.AddField(
            model_name='epizoda',
            name='epizode_preuzmi',
            field=models.CharField(default='', max_length=300),
        ),
    ]
