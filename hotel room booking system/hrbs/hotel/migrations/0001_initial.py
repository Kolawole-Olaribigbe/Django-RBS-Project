# Generated by Django 5.0.4 on 2024-04-20 14:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.IntegerField()),
                ('room_no', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type_id', models.IntegerField()),
                ('room_type', models.CharField(choices=[('SIN', 'SINGLE ROOM'), ('FAM', 'FAMILY ROOM'), ('DEL', 'DELUXE ROOM')], max_length=12)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(choices=[('paid', 'Paid'), ('pending', 'Pending'), ('processing', 'Processing'), ('cancelled', 'Cancelled'), ('initiated', 'Initiated'), ('failed', 'Failed'), ('refunding', 'Refunding'), ('refunded', 'Refunded'), ('unpaid', 'Unpaid'), ('expired', 'Expired')], max_length=100)),
                ('check_in_date', models.DateTimeField()),
                ('check_out_date', models.DateTimeField()),
                ('no_of_guests', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.room')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='room_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.roomtype'),
        ),
    ]
