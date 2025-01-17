# Generated by Django 4.2.17 on 2024-12-21 14:36

from django.db import migrations, models
import django.db.models.deletion
import flights.models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airplane',
            name='capacity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='airplane',
            name='model',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='airplane',
            name='production_year',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='airplane',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='airplane',
            name='tail_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='flight',
            name='airplane',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flights', to='flights.airplane'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='flight_number',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='flights.flight'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='passenger_email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='passenger_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reservation_code',
            field=models.CharField(default=flights.models.generate_reservation_code, max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
