# Generated by Django 4.1 on 2023-03-01 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estimator', '0003_delete_housing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Housing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zipcode', models.IntegerField()),
                ('surface', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('floors', models.IntegerField()),
                ('waterfront', models.IntegerField()),
                ('condition', models.IntegerField()),
                ('bathbed_ratio', models.FloatField()),
                ('estimation', models.IntegerField()),
            ],
        ),
    ]
