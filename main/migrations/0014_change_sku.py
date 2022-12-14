# Generated by Django 3.2.16 on 2022-12-10 18:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20221210_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('raw', models.ManyToManyField(blank=True, null=True, to='main.Raw')),
            ],
        ),
        migrations.CreateModel(
            name='Change',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=200)),
                ('status', models.BooleanField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('raw_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.raw')),
            ],
        ),
    ]
