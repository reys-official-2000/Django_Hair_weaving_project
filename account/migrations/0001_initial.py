# Generated by Django 5.1.1 on 2024-09-13 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/users')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('token', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('code', models.CharField(blank=True, max_length=6, null=True)),
                ('token_created_at', models.DateTimeField(blank=True, null=True)),
                ('code_created_at', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
