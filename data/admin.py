from django.contrib import admin

from .models import Ingredient, Recipe, RecipeIngredient, Favorite


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1
    raw_id_fields = ['ingredient']


class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'dimension']
    search_fields = ['name']
    list_filter = ['name']


class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'tag', 'pub_date']
    list_filter = ['author', 'name']
    inlines = [RecipeIngredientInline]       


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient)
admin.site.register(Favorite)
