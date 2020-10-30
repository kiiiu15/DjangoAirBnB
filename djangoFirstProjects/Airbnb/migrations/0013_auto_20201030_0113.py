# Generated by Django 2.2.12 on 2020-10-30 01:13

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Airbnb', '0012_auto_20201028_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='maxPeople',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='property',
            name='photo',
            field=models.ImageField(upload_to='gallery'),
        ),
        migrations.AlterField(
            model_name='property',
            name='pricePerDay',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='code',
            field=models.CharField(default='2020-10-30 01:13:45.285237+00:00', max_length=70),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 10, 30, 1, 13, 45, 285206, tzinfo=utc)),
        ),
    ]
