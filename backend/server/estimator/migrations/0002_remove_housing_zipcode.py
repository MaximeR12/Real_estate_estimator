# Generated by Django 4.1 on 2023-02-27 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estimator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='housing',
            name='zipcode',
        ),
    ]
