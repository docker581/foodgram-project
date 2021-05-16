# Generated by Django 3.0.5 on 2021-05-14 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_auto_20210514_0304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='classname',
        ),
        migrations.AddField(
            model_name='tag',
            name='badge_class',
            field=models.CharField(default='one', max_length=50, verbose_name='Класс для значка'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='checkbox_class',
            field=models.CharField(default='two', max_length=50, verbose_name='Класс для чекбокса'),
            preserve_default=False,
        ),
    ]