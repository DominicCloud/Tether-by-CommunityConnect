# Generated by Django 4.2.6 on 2023-11-02 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tether', '0005_campaignregistration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaignregistration',
            name='date_of_registration',
            field=models.DateTimeField(),
        ),
    ]
