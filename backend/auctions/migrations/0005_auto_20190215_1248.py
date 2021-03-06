# Generated by Django 2.1.7 on 2019-02-15 12:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_ad_minimum_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='ad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='auctions.Ad', verbose_name='ad'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='bidder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to=settings.AUTH_USER_MODEL, verbose_name='bidder'),
        ),
    ]
