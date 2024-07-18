# Generated by Django 5.0 on 2024-07-17 13:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_flightbooking_booking_date_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotelbooking',
            name='hotel',
        ),
        migrations.RemoveField(
            model_name='hotelbooking',
            name='user',
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin_date', models.DateField(blank=True, null=True)),
                ('checkout_date', models.DateField(blank=True, null=True)),
                ('departure_date', models.DateField(blank=True, null=True)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('number_of_adults', models.PositiveIntegerField(blank=True, null=True)),
                ('number_of_children', models.PositiveIntegerField(blank=True, null=True)),
                ('number_of_seats', models.PositiveIntegerField(blank=True, null=True)),
                ('total_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('flight', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.flight')),
                ('hotel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.hotel')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='FlightBooking',
        ),
        migrations.DeleteModel(
            name='HotelBooking',
        ),
    ]
