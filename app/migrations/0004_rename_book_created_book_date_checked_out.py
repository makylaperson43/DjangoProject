# Generated by Django 3.2.8 on 2021-11-19 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_book_book_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='book_created',
            new_name='date_checked_out',
        ),
    ]
