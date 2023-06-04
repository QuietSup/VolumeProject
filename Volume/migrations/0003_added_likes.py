# Generated by Django 4.2.1 on 2023-06-04 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Volume', '0002_made_email_not_unique'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pin',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='user',
            name='liked_pins',
            field=models.ManyToManyField(related_name='liked_users', to='Volume.pin'),
        ),
    ]
