# Generated by Django 3.1.4 on 2020-12-04 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='breakfast',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]