# Generated by Django 4.2.6 on 2023-11-02 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tether', '0002_campaigns'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaigns',
            name='bgimg',
            field=models.ImageField(blank=True, null=True, upload_to='S:\\Django Python\\CommunityConnect_SemV\\static\\images'),
        ),
    ]
