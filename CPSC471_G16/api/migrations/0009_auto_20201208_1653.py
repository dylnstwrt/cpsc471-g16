# Generated by Django 3.1.4 on 2020-12-08 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20201208_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='message',
            field=models.CharField(default='', editable=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='sale',
            name='profit',
            field=models.FloatField(default=0.0),
        ),
    ]