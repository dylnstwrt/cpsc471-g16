# Generated by Django 3.1.4 on 2020-12-08 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_distributes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basket',
            old_name='basket_item',
            new_name='upc',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='sales_tax',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='subtotal',
            field=models.FloatField(default=0.0),
        ),
    ]