# Generated by Django 4.2.6 on 2023-11-02 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tether', '0003_alter_campaigns_bgimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('campaign_type', models.TextField()),
                ('description', models.TextField()),
                ('doe', models.DateTimeField()),
                ('tags_arr', models.JSONField()),
                ('bgimg', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('contact_info', models.JSONField()),
            ],
        ),
        migrations.DeleteModel(
            name='Campaigns',
        ),
    ]