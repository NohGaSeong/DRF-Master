# Generated by Django 4.1.3 on 2022-12-03 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_verified',
            field=models.BooleanField(default=False, help_text='Designates whether this users email is verified. ', verbose_name='email_verified'),
        ),
    ]
