# Generated by Django 5.0.6 on 2024-06-09 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_customer_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
