# Generated by Django 3.1.1 on 2022-05-02 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('floodreport', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='floodreport',
            old_name='Messgae',
            new_name='Message',
        ),
    ]
