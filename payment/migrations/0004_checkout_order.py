# Generated by Django 5.1.3 on 2025-01-09 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_alter_checkout_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='Order',
            field=models.BooleanField(default=False),
        ),
    ]