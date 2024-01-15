from django.contrib import admin

from recipes.models import Category, Recipe

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name',)
    search_fields = ('name',)
    ordering = ('id',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...
    # list_display = ('title', 'description', 'category', 'is_published')
    # fields = (
    #     'title', 'description', 'slug', 'preparation_time',
    #     'preparation_time_unit', 'servings', 'servings_unit',
    #     'preparation_steps', 'preparation_steps_is_html',
    #     'is_published', 'cover', 'category', 'author'
    # )
    # search_fields = ('title', 'description', 'category__name')
    # ordering = ('id',)
    # list_filter = ('category', 'is_published')
    # autocomplete_fields = ('category', 'author')
    readonly_fields = ('id', 'created_at', 'updated_at')


admin.site.register(Category, CategoryAdmin)
# admin.site.register(Recipe, RecipeAdmin)
