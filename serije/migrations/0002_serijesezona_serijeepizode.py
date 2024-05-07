# Generated by Django 5.0.4 on 2024-04-22 15:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serije', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SerijeSezona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sezona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serije.serije')),
            ],
        ),
        migrations.CreateModel(
            name='SerijeEpizode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epizode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serije.serijesezona')),
            ],
        ),
    ]