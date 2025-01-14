# Generated by Django 4.2.6 on 2023-11-02 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tether', '0004_campaign_delete_campaigns'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampaignRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign_title', models.CharField(max_length=100)),
                ('date_of_registration', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tether.profile')),
            ],
        ),
    ]
