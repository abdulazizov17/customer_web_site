# Generated by Django 5.1 on 2024-08-13 10:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_alter_customer_table_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='FM',
            field=models.CharField(default=django.utils.timezone.now, max_length=120),
            preserve_default=False,
        ),
    ]