from django import forms

from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'name',
            'tags',
            'time',
            'description',
            'image',
            'slug',
        )
        widgets = {
            'description': forms.Textarea(attrs={'rows': 8}),
            'tags': forms.CheckboxSelectMultiple(),
        }
