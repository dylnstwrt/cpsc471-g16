# Generated by Django 3.1.4 on 2020-12-08 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20201208_1555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basket',
            old_name='upc_otm',
            new_name='basket_item',
        ),
    ]
