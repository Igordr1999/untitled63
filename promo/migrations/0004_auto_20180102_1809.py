# Generated by Django 2.0.1 on 2018-01-02 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promo', '0003_radiostation_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radiostation',
            name='logo',
            field=models.ImageField(default='radio/logo/default.png', upload_to='radio/logo/'),
        ),
    ]
