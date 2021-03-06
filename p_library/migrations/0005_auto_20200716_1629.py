# Generated by Django 3.0.8 on 2020-07-16 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0004_auto_20200716_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='copy_count',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
