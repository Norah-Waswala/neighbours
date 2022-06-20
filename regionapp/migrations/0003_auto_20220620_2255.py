# Generated by Django 2.2.26 on 2022-06-20 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regionapp', '0002_auto_20220620_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbourhood',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='image',
            field=models.ImageField(default='default.png', upload_to='images/'),
        ),
    ]