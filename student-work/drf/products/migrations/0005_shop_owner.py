# Generated by Django 5.0.7 on 2024-07-10 20:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_shop_product_shop"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="shop",
            name="owner",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
