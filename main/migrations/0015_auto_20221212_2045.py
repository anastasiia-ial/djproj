# Generated by Django 3.2.16 on 2022-12-12 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_change_sku'),
    ]

    operations = [
        migrations.AddField(
            model_name='sku',
            name='photo',
            field=models.IntegerField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='sku',
            name='weight',
            field=models.IntegerField(blank=True, max_length=3, null=True),
        ),
    ]
