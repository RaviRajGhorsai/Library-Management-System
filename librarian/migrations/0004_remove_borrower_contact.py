# Generated by Django 5.0.1 on 2024-02-03 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0003_remove_borrower_membership_id_borrower_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrower',
            name='contact',
        ),
    ]
