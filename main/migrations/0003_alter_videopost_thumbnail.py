# Generated by Django 3.2.4 on 2021-06-18 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210617_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videopost',
            name='thumbnail',
            field=models.ImageField(default='none', null=True, upload_to='videos/thumbnail/'),
        ),
    ]
