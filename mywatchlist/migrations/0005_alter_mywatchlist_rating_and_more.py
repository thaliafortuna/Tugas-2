# Generated by Django 4.1 on 2022-09-21 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0004_alter_mywatchlist_rating_alter_mywatchlist_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywatchlist',
            name='rating',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='mywatchlist',
            name='release_date',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='mywatchlist',
            name='review',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='mywatchlist',
            name='title',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='mywatchlist',
            name='watched',
            field=models.CharField(max_length=300, null=True),
        ),
    ]