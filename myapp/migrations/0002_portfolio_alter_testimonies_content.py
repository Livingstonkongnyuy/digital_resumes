# Generated by Django 4.2 on 2023-05-07 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='media/portfolio')),
                ('url', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name': 'Portfolio',
                'verbose_name_plural': 'Portfolio',
            },
        ),
        migrations.AlterField(
            model_name='testimonies',
            name='content',
            field=models.CharField(max_length=275),
        ),
    ]
