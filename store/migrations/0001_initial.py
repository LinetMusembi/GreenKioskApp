# Generated by Django 4.2.1 on 2023-06-21 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity', models.PositiveBigIntegerField()),
                ('category', models.CharField(max_length=70)),
                ('store_name', models.CharField(max_length=50)),
                ('store_location', models.CharField(max_length=70)),
            ],
        ),
    ]
