# Generated by Django 5.1.1 on 2024-10-03 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0006_address_author_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Address Entries'},
        ),
        migrations.RemoveField(
            model_name='address',
            name='country',
        ),
    ]
