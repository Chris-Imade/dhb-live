# Generated by Django 4.1.6 on 2023-02-25 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_transaction_transation_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='transation_state',
            new_name='transaction_state',
        ),
    ]