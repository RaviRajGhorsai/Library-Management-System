# Generated by Django 5.0.1 on 2024-02-06 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0009_remove_transaction_return_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='contact',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
