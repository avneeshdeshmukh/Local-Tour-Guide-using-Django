# Generated by Django 5.0 on 2024-04-12 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TourApp', '0005_remove_restaurantimage_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantreview',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
