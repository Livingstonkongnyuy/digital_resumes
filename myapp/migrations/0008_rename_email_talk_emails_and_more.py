# Generated by Django 4.2 on 2023-05-14 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_rename_contacts_talk_alter_talk_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='talk',
            old_name='email',
            new_name='emails',
        ),
        migrations.RenameField(
            model_name='talk',
            old_name='message',
            new_name='messages',
        ),
        migrations.RenameField(
            model_name='talk',
            old_name='name',
            new_name='names',
        ),
    ]