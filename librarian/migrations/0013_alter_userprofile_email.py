# Generated by Django 5.0.1 on 2024-02-06 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0012_userprofile_address_userprofile_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
