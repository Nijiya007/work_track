# Generated by Django 5.1.4 on 2025-01-06 09:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('velvetekapp', '0007_alter_apply_estimation_document_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuelCharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technician_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('purpose', models.TextField()),
                ('kilometers', models.FloatField()),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('customer_name', models.CharField(max_length=225)),
                ('issue', models.TextField()),
                ('apply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fuel_charges', to='velvetekapp.apply')),
            ],
        ),
    ]
