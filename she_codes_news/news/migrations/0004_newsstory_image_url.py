# Generated by Django 4.2.2 on 2023-07-08 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_newsstory_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='image_url',
            field=models.CharField(default='placeholder-3.jpg', max_length=200),
        ),
    ]
