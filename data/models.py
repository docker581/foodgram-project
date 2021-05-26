from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.constraints import UniqueConstraint

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Название тега',
    )
    color = models.CharField(
        max_length=50,
        verbose_name='Цвет тега',
    )
    template_id = models.CharField(
        max_length=50,
        verbose_name='Название для атрибута id в шаблоне',
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name    


class Ingredient(models.Model):
    name = models.CharField(
        max_length=100, 
        verbose_name='Название ингредиента',
    )
    dimension = models.CharField(
        max_length=50, 
        verbose_name='Единица измерения',
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return f'Ингредиент {self.name} ({self.dimension})'


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор',
    )
    name = models.CharField(max_length=50, verbose_name = 'Название рецепта')
    image = models.ImageField(
        upload_to='data/', 
        blank=True, 
        null=True,
        verbose_name='Изображение',
    )
    description = models.TextField(verbose_name='Описание')
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        verbose_name='Ингредиенты',
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='tags',
        verbose_name='Теги',
    )
    time = models.PositiveIntegerField(verbose_name='Время приготовления')
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='URL-имя',
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
        db_index=True,
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
    )
    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.CASCADE,
        verbose_name='Ингредиент',    
    )
    quantity = models.PositiveIntegerField(verbose_name='Количество')

    class Meta:
        verbose_name = 'Ингредиент для рецепта'
        verbose_name_plural = 'Ингредиенты для рецепта'   

    def __str__(self):
        return f'{self.ingredient} для {self.recipe}'     


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Рецепт',
    )

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_user_recipe',
            )
        ]
        verbose_name = 'Избранный рецепт'
        verbose_name_plural = 'Избранное'

    def __str__(self):
        return f'Избранный рецепт {self.recipe} у {self.user}'

        
class Subscription(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
        verbose_name='Автор',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='authors',
        verbose_name='Подписчик',
    )

    class Meta:
        models.UniqueConstraint(
            fields=['author', 'user'],
            name='unique_author_user',
        )
        verbose_name = 'Подписка'
        verbose_name_plural='Подписки'
    
    def __str__(self):
        return f'Подписка на {self.author} у {self.user}'           


class Purchase(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='purchases',
        verbose_name='Пользователь',
    )
    purchase = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='purchases',
        verbose_name='Покупка',
    )

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['user', 'purchase'],
                name='unique_user_purchase',
            )
        ]
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'

    def __str__(self):
        return f'Покупка {self.purchase} у {self.user}'
