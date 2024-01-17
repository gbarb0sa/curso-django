from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ('id',)


class Recipe(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    description = models.CharField(max_length=200, verbose_name='Descrição')
    slug = models.SlugField(unique=True)
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=50)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=50)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(
        upload_to='recipes/covers/%Y/%m/%d/', blank=True, default='')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True,
        blank=True, default=None)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'
        ordering = ('id',)
