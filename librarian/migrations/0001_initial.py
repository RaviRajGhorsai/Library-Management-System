# Generated by Django 5.0.1 on 2024-02-02 06:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('birthdate', models.DateTimeField()),
                ('nationality', models.CharField(max_length=20)),
                ('biography', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('contact', models.IntegerField()),
                ('membership_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=20)),
                ('contact', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LibraryBranch',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=20)),
                ('benefits', models.CharField(max_length=150)),
                ('fees', models.CharField(max_length=10)),
                ('duration', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=20)),
                ('publication_date', models.DateTimeField()),
                ('description', models.CharField(max_length=150)),
                ('quantity_avilable', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='librarian.author')),
            ],
        ),
        migrations.CreateModel(
            name='Fine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('reason', models.CharField(max_length=100)),
                ('date_imposed', models.DateTimeField()),
                ('borrower_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='librarian.borrower')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_reserved', models.DateTimeField()),
                ('expiry_id', models.DateTimeField()),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='librarian.book')),
                ('borrower_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='librarian.borrower')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_borrowed', models.DateTimeField()),
                ('due_date', models.DateTimeField()),
                ('return_date', models.DateTimeField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='librarian.book')),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='librarian.borrower')),
            ],
        ),
    ]