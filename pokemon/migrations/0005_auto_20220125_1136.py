# Generated by Django 2.2.26 on 2022-01-25 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0004_auto_20220125_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='personagem',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='upload',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
    ]
