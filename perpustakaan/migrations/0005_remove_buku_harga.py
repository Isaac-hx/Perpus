# Generated by Django 4.2.7 on 2024-01-08 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0004_buku_harga'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buku',
            name='harga',
        ),
    ]
