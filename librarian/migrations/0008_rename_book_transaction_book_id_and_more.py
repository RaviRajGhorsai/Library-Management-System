# Generated by Django 5.0.1 on 2024-02-03 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0007_rename_quantity_avilable_book_quantity_available'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='book',
            new_name='book_id',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='borrower',
            new_name='borrower_id',
        ),
    ]
