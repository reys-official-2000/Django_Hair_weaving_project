# Generated by Django 5.1.1 on 2024-09-13 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0002_remove_texturemodel_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TextureModel',
            new_name='Model',
        ),
    ]
