from django.db import models


class Category(models.Model):
    title = models.CharField('categoria', max_length=50, unique=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField('título', max_length=100, unique=True)
    price = models.DecimalField('preço', max_digits=8, decimal_places=2)
    category = models.ForeignKey(
        Category,
        verbose_name='categoria',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('title',)
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'

    def __str__(self):
        return self.title
