# Generated by Django 4.2 on 2023-05-14 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Contacts',
        ),
        migrations.AlterModelOptions(
            name='contacts',
            options={'verbose_name': 'Contacts', 'verbose_name_plural': 'Contacts'},
        ),
    ]
