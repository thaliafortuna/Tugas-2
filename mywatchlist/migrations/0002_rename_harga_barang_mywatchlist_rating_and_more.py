# Generated by Django 4.1 on 2022-09-20 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mywatchlist',
            old_name='harga_barang',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='mywatchlist',
            old_name='deskripsi',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='mywatchlist',
            name='nama_barang',
        ),
        migrations.AddField(
            model_name='mywatchlist',
            name='release_date',
            field=models.CharField(max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='mywatchlist',
            name='review',
            field=models.CharField(max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='mywatchlist',
            name='watched',
            field=models.CharField(max_length=140, null=True),
        ),
    ]