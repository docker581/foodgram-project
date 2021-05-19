from django.contrib import admin

from .models import Ingredient, Tag, Recipe, RecipeIngredient, Favorite


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1
    raw_id_fields = ['ingredient']
    list_display = ['recipe', 'ingredient', 'id']


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'color']  


class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'dimension']
    search_fields = ['name']
    list_filter = ['name']


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ['name', 'author', 'pub_date']
    list_filter = ['author', 'name']       


admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient)
admin.site.register(Favorite)
