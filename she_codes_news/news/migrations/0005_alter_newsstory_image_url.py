# Generated by Django 4.2.2 on 2023-07-18 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_remove_newsstory_author_id_alter_newsstory_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='image_url',
            field=models.URLField(default='placeholder-3.jpg'),
        ),
    ]
