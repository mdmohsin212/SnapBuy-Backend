# Generated by Django 5.1.3 on 2025-01-10 14:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0008_remove_orderditem_product_orderditem_product'),
        ('product', '0007_alter_category_slug_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderditem',
            name='product',
        ),
        migrations.AddField(
            model_name='orderditem',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]