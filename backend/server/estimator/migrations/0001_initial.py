# Generated by Django 4.1 on 2023-02-27 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Housing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zipcode', models.IntegerField()),
                ('surface', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('estimation', models.IntegerField()),
            ],
        ),
    ]
