# Generated by Django 5.1.3 on 2025-01-26 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
    ]
