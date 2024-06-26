# Generated by Django 5.0.4 on 2024-04-22 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmovi', '0004_filmovi_datum_filmovi_godina_filmovi_imdb_ocena_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filmovi',
            old_name='datum',
            new_name='date',
        ),
        migrations.AlterField(
            model_name='filmovi',
            name='godina',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='filmovi',
            name='image',
            field=models.FileField(upload_to='movie-images'),
        ),
        migrations.AlterField(
            model_name='filmovi',
            name='imdb_ocena',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='filmovi',
            name='originalni_naziv',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='filmovi',
            name='zanr',
            field=models.CharField(max_length=120),
        ),
    ]
