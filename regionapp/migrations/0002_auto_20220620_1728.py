# Generated by Django 2.2.26 on 2022-06-20 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regionapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighbourhood',
            name='description',
        ),
        migrations.RemoveField(
            model_name='neighbourhood',
            name='image',
        ),
    ]
