# Generated by Django 5.1.4 on 2025-01-01 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('velvetekapp', '0003_alter_customer_reffered_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='photos_of_item',
            field=models.ImageField(blank=True, null=True, upload_to='apply'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='work_type',
            field=models.CharField(choices=[('sale', 'sale'), ('service', 'service')], default=True, max_length=10),
        ),
        migrations.DeleteModel(
            name='ApplyImage',
        ),
    ]
