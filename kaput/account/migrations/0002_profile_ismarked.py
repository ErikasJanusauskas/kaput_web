# Generated by Django 4.2.5 on 2024-01-30 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='isMarked',
            field=models.BooleanField(default=False),
        ),
    ]
