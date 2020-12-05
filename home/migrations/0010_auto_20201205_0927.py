# Generated by Django 3.1.4 on 2020-12-05 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20201205_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='order_name_dinner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='apply_order_dinner', to='home.dinner'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_name_lunch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='apply_order_lunch', to='home.lunch'),
        ),
    ]
