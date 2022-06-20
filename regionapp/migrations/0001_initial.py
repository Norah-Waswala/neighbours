# Generated by Django 2.2.26 on 2022-06-20 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NeighbourHood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=60)),
                ('image', models.ImageField(default='default.png', upload_to='images/')),
                ('health_tell', models.IntegerField(blank=True, null=True)),
                ('police_number', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField()),
                ('Occupants_Count', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=80)),
                ('profile_picture', models.ImageField(default='default.png', upload_to='images/')),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=80)),
                ('neighbourhood', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='regionapp.NeighbourHood')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, null=True)),
                ('post', models.TextField()),
                ('post_picture', models.ImageField(default='default.png', upload_to='images/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='region_post', to='regionapp.NeighbourHood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_owner', to='regionapp.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hood', to='regionapp.Profile'),
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('business_picture', models.ImageField(default='default.png', upload_to='images/')),
                ('description', models.TextField(blank=True)),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business', to='regionapp.NeighbourHood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='regionapp.Profile')),
            ],
        ),
    ]