# Generated by Django 3.1.4 on 2020-12-04 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_breakfast_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lunch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='media')),
                ('desc', models.TextField(blank=True, null=True)),
            ],
        ),
    ]