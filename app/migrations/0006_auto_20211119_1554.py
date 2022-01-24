# Generated by Django 3.2.8 on 2021-11-19 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_book_date_returned'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='date_returned',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=200, null=True),
        ),
    ]