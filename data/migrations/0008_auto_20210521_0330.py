# Generated by Django 3.0.5 on 2021-05-21 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_auto_20210517_1555'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['-pub_date'], 'verbose_name': 'Рецепт', 'verbose_name_plural': 'Рецепты'},
        ),
    ]