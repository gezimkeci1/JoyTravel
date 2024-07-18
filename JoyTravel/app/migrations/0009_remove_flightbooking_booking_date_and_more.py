# Generated by Django 5.0 on 2024-07-17 12:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_flightbooking_hotelbooking'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flightbooking',
            name='booking_date',
        ),
        migrations.RemoveField(
            model_name='hotelbooking',
            name='booking_date',
        ),
        migrations.AddField(
            model_name='flightbooking',
            name='departure_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='flightbooking',
            name='return_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flightbooking',
            name='flight',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.flight'),
        ),
        migrations.AlterField(
            model_name='flightbooking',
            name='seats',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flightbooking',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='flightbooking',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='adults',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='checkin_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='checkout_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='children',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='hotel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.hotel'),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
