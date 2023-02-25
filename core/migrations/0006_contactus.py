# Generated by Django 4.1.6 on 2023-02-25 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_newsletter'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Client Name')),
                ('email', models.CharField(max_length=100, verbose_name='Client Email')),
                ('message', models.TextField(max_length=1000, verbose_name='Client Email')),
            ],
        ),
    ]
