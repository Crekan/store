from django.db import models

from users.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=250, unique=True, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория продукта'
        verbose_name_plural = 'Категории продукта'


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='В наличии')
    image = models.ImageField(upload_to='products_images/', blank=True, verbose_name='Фото')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class BasketQuerySet(models.QuerySet):
    def total_quantity(self):
        return sum(basket.quantity for basket in self)

    def total_sum(self):
        return sum(basket.sum() for basket in self)


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='')
    quantity = models.PositiveIntegerField(default=0, verbose_name='')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='')

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

    def sum(self):
        return self.product.price * self.quantity
