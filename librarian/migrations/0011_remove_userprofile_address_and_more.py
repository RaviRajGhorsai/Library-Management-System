# Generated by Django 5.0.1 on 2024-02-06 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0010_userprofile_address_userprofile_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='contact',
        ),
    ]