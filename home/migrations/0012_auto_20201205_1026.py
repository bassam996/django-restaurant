# Generated by Django 3.1.4 on 2020-12-05 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20201205_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='ordered_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
