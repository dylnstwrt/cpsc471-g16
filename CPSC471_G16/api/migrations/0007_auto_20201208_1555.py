# Generated by Django 3.1.4 on 2020-12-08 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20201208_0852'),
    ]

    operations = [
        migrations.RenameField(
            model_name='distributes',
            old_name='item_upd',
            new_name='item_upc',
        ),
        migrations.RemoveField(
            model_name='basket',
            name='upc',
        ),
        migrations.AddField(
            model_name='basket',
            name='upc_otm',
            field=models.ManyToManyField(to='api.Item'),
        ),
    ]
