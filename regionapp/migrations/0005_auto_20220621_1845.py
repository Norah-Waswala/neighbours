# Generated by Django 2.2.26 on 2022-06-21 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regionapp', '0004_auto_20220621_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='business_picture',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
