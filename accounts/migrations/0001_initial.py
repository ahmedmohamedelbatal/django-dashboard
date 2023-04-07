# Generated by Django 4.2 on 2023-04-07 18:52

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(default='not found', max_length=100)),
                ('address', models.CharField(default='not found', max_length=100)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], default='not found', max_length=100)),
                ('phone', models.CharField(default='not found', max_length=12)),
                ('image', models.ImageField(upload_to='profiles/')),
                ('biography', models.TextField(default='not found', max_length=300)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]