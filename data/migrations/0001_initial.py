# Generated by Django 3.0.5 on 2021-05-11 00:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название ингредиента')),
                ('dimension', models.CharField(max_length=50, verbose_name='Единица измерения')),
            ],
            options={
                'verbose_name_plural': 'Ингредиенты',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название рецепта')),
                ('image', models.ImageField(blank=True, null=True, upload_to='data/', verbose_name='Изображение')),
                ('description', models.TextField(verbose_name='Описание')),
                ('tag', multiselectfield.db.fields.MultiSelectField(choices=[('завтрак', 'завтрак'), ('обед', 'обед'), ('ужин', 'ужин')], max_length=17, verbose_name='Тег')),
                ('time', models.PositiveIntegerField(verbose_name='Время приготовления')),
                ('slug', models.SlugField(unique=True, verbose_name='URL-имя')),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name_plural': 'Рецепты',
                'ordering': ['pub_date'],
            },
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Ingredient', verbose_name='Ингредиент')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Recipe', verbose_name='Рецепт')),
            ],
            options={
                'verbose_name_plural': 'Ингредиенты для рецепта',
            },
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(through='data.RecipeIngredient', to='data.Ingredient', verbose_name='Ингредиенты'),
        ),
    ]
