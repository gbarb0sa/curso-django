from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ('id',)


class Recipe(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    description = models.CharField(max_length=200, verbose_name='Descrição')
    slug = models.SlugField(unique=True, verbose_name='Slug')
    preparation_time = models.IntegerField(verbose_name='Tempo de preparo')
    preparation_time_unit = models.CharField(
        max_length=50, verbose_name='Unidade de tempo de preparo')
    servings = models.IntegerField(verbose_name='Porções')
    servings_unit = models.CharField(
        max_length=50, verbose_name='Unidade de porções')
    preparation_steps = models.TextField(verbose_name='Como preparar')
    preparation_steps_is_html = models.BooleanField(
        default=False, verbose_name='Como preparar está em HTML?')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(
        default=False, verbose_name='Está publicada?')
    cover = models.ImageField(
        upload_to='recipes/covers/%Y/%m/%d/', blank=True, default='',
        verbose_name='Imagem')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True,
        blank=True, default=None, verbose_name='Categoria')
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, verbose_name='Autor')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'recipes'
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'
        ordering = ('id',)
