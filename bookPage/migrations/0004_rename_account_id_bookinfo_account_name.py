# Generated by Django 5.1.3 on 2024-11-26 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookPage', '0003_account_bookinfo_account_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinfo',
            old_name='account_id',
            new_name='account_name',
        ),
    ]
